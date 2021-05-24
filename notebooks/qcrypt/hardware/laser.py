r"""
Provides a class that can send a bit with a laser connected via a relay.

Handles logging and MQTT communication over the classical channel.
"""

# standard library:
import time
import logging

# third party:
import paho.mqtt.client as mqtt

try:
    from . import relay_lib_seeed
except Exception as e:
    print(f'{type(e).__name__}: {e},')


class Laser:
    """
    Represents a sinle laser that is controlled by a relay.
    """
    # executed at import:
    logger = logging.getLogger("__Laser__")
    formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s")
    streamhandler = logging.StreamHandler()
    filehandler = logging.FileHandler(filename="laser.log", mode="a")
    streamhandler.setFormatter(formatter)
    filehandler.setFormatter(formatter)
    logger.addHandler(streamhandler)
    logger.addHandler(filehandler)

    def __init__(
        self,
        username="alice",
        relay_id=1,
        delay_in_seconds=1,
        mqtt_broker_ip="localhost",
        log_level="INFO",
    ):
        """
        Construct a Laser.
        """
        self.username = username
        self.relay_id = relay_id
        self.delay_in_seconds = delay_in_seconds
        self.laser_channel = (
            f"quantum_cryptography/classical_channel/{username}/laser"
        )
        self.logger.setLevel(log_level)

        self.logger.debug(f"{username} relay: selected number {relay_id}")
        self.logger.debug(
            f"{username} delay between on and off: {delay_in_seconds}s"
        )
        self.logger.debug(f"{username} mqtt_broker_ip: {mqtt_broker_ip}")

        self.mqtt_broker_ip = mqtt_broker_ip
        self.log_level = log_level

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect

        self.client.connect(mqtt_broker_ip, 1883, 60)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        self.logger.info(f"mqtt: {self.username} connected")

    def on_disconnect(self, client, userdata, rc):
        self.logger.warning(f"mqtt: {self.username} disconnected")

    def trigger(self):
        """
        Trigger the laser and communicate it over the classical channel.
        """
        self.logger = logging.getLogger("__Laser__")
        self.client.publish(
            self.laser_channel, payload="on", qos=0, retain=False
        )
        relay_lib_seeed.relay_on(self.relay_id)
        self.logger.info(f"{self.username} laser relay {self.relay_id}: on")

        time.sleep(self.delay_in_seconds)

        self.client.publish(
            self.laser_channel, payload="off", qos=0, retain=False
        )
        relay_lib_seeed.relay_off(self.relay_id)
        self.logger.info(f"{self.username} laser relay {self.relay_id}: off")
