# standard libraries:
import time
import logging
import enum

# third party:
import paho.mqtt.client as mqtt

try:
    import RPi.GPIO as GPIO

    HARDWARE_IMPORTS = True
except ModuleNotFoundError as exception:
    print(f"{type(exception).__name__}: {exception}")
    HARDWARE_IMPORTS = False


class Orientation(enum.IntEnum):
    LEFT = 0  # -45°.
    VERTICAL = 1  # 0°.
    RIGHT = 2  # 45°.
    HORIZONTAL = 3  # 90°.


class Filterwheel:

    # executed at import:
    # logging
    logger = logging.getLogger("__Filterwheel__")
    formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s")
    streamhandler = logging.StreamHandler()
    filehandler = logging.FileHandler(filename="filterwheel.log", mode="a")
    streamhandler.setFormatter(formatter)
    filehandler.setFormatter(formatter)
    logger.addHandler(streamhandler)
    logger.addHandler(filehandler)

    def __init__(
        self,
        username="Alice",
        dir_pin=26,
        step_pin=21,
        delay_in_seconds=0.0025,
        mqtt_broker_ip="localhost",
        log_level="INFO",
    ):

        """
        Construct a Filterwheel
        """
        self.username = username
        self.dir_pin = dir_pin
        self.step_pin = step_pin
        self.delay_in_seconds = delay_in_seconds
        self.mqtt_broker_ip = mqtt_broker_ip
        self.log_level = log_level
        self.orientation = Orientation.VERTICAL

        self.logger.setLevel(log_level)

        if HARDWARE_IMPORTS:
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(dir_pin, GPIO.OUT)
            GPIO.setup(step_pin, GPIO.OUT)

        else:
            self.logger.error(
                "failed to import required hardware modules: "
                "### Continuing in simulation mode ... ###"
            )

    def rotate_to(self, orientation):
        start = self.orientation
        stop = orientation
        print(start, "-->", stop)
        if start == stop:
            print("no need to rotate")
        elif abs(start - stop) == 2:
            print("rotating 180°")
            self._rotate(clockwise=True, steps=100)
        else:
            diff = abs(start - stop)
            if diff == 1:
                if start > stop:
                    print("rotating right")
                    self._rotate(clockwise=True)
                else:
                    print("rotating left")
                    self._rotate(clockwise=False)
            if diff == 3:
                if start < stop:
                    print("rotating right")
                    self._rotate(clockwise=True)
                else:
                    print("rotating left")
                    self._rotate(clockwise=False)
                    
        self.orientation = orientation

    def _rotate(self, clockwise=True, steps=50):
        """
        Rotates in "dir" direction "steps" time
        """

        if HARDWARE_IMPORTS:
            GPIO.output(self.dir_pin, clockwise)

            for x in range(steps):
                GPIO.output(self.step_pin, GPIO.HIGH)
                time.sleep(self.delay_in_seconds)
                GPIO.output(self.step_pin, GPIO.LOW)
                time.sleep(self.delay_in_seconds)

        if clockwise:
            direction = "clockwise"
        else:
            direction = "counter-clockwise"

        self.logger.info(f"{self.username} rotating {steps} steps {direction}")

    def on_connect(self, client, userdata, flags, rc):
        """
        called on MQTT connection
        """
        self.logger.info(f"mqtt: {self.username} connected")

    def on_disconnect(self, client, userdata, rc):
        """
        called on MQTT disconnection
        """
        self.logger.warning(f"mqtt: {self.username} disconnected")
