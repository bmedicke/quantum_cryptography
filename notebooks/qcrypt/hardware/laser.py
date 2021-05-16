import time
import logging
import paho.mqtt.client as mqtt
from . import relay_lib_seeed


class Laser:
    def __init__(
        self,
        username="alice",
        relay_id=1,
        delay_in_seconds=1,
        mqtt_broker_ip="localhost",
    ):

        self.name = username
        self.relay = relay_id
        self.delay = delay_in_seconds
        self.laser_channel = (
            f"quantum_cryptography/classical_channel/{username}/laser"
        )

        logging.info(f"{username} relay: selected number {relay_id}")
        logging.info(f"{username} delay between on and off: {delay_in_seconds}s")

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect

        self.client.connect(mqtt_broker_ip, 1883, 60)
        self.client.loop_start()

    logging.basicConfig(
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(filename="laser.log", mode="a"),
        ],
        format="%(asctime)s: %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    logging.info("laser module: imported")

    def on_connect(self, client, userdata, flags, rc):
        logging.info(f"mqtt: {self.name} connected")

    def on_disconnect(self, client, userdata, rc):
        logging.warning(f"mqtt: {self.name} disconnected")

    def trigger(self):
        self.client.publish(
            self.laser_channel, payload="on", qos=0, retain=False
        )
        relay_lib_seeed.relay_on(self.relay)
        logging.info(f"{self.name} laser relay {self.relay}: on")

        time.sleep(self.delay)

        self.client.publish(
            self.laser_channel, payload="off", qos=0, retain=False
        )
        relay_lib_seeed.relay_off(self.relay)
        logging.info(f"{self.name} laser relay {self.relay}: off")
