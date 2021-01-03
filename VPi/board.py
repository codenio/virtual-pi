import os

BOARD = os.getenv('BOARD')

if BOARD == "raspi_40pin":
    from raspberrypi.raspi_40pin import *

elif BOARD == "raspberry_pi_cm":
    from raspberrypi.raspi_cm import *

elif BOARD == "RASPBERRY_PI_B_REV1":
    from raspberrypi.raspi_1b_rev1 import *

elif BOARD == "RASPBERRY_PI_A" or BOARD == "RASPBERRY_PI_B_REV2":
    from raspberrypi.raspi_1b_rev2 import *
else:
	# by default load RPI B rev 2
	from raspberrypi.raspi_1b_rev2 import *

def I2C():
    """The singleton I2C interface"""
    import busio

    return busio.I2C(SCL, SDA)


def SPI():
    """The singleton SPI interface"""
    import busio

    return busio.SPI(SCLK, MOSI, MISO)