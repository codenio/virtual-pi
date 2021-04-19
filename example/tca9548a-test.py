'''

Python Script for seeting voltages to 5 MCP4725 DAC units multiplexed using TCA9548a

Use : Helps to check if 5 DAC units Multiplexed with I2X Mux is working properly

'''
try:
    import RPi.GPIO as GPIO
    import board
    import busio
    import adafruit_tca9548a
    import adafruit_mcp4725
except:
    import VPi.GPIO as GPIO
    import VPi.board as board
    import VPi.busio as busio
    import VPi.adafruit_tca9548a as adafruit_tca9548a
    import VPi.adafruit_mcp4725 as adafruit_mcp4725

import time

# Disable Active Low Reset of I2C MUX
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, GPIO.HIGH)

time.sleep(5)

# Using I2C channel 1
I2C1_SDA_PIN = 2
I2C1_SCL_PIN = 3

# For Channel 0
# GPIO 0, Board Pin Numbers 27
# GPIO 1, Board Pin Numbers 28

# Initialize I2C bus.
i2c = busio.I2C(I2C1_SCL_PIN,I2C1_SDA_PIN)
# default TCA address=0x70
tca = adafruit_tca9548a.TCA9548A(i2c)

print("attempting to connect to DAC")
# Initialize all 5 MCP4725 at default address=0x60
time.sleep(1)
dac1 = adafruit_mcp4725.MCP4725(tca[0], address=0x60)
print("connected to MCP on tca[0]")
input("Press enter...")
time.sleep(1)
dac2 = adafruit_mcp4725.MCP4725(tca[1], address=0x60)
print("connected to MCP on tca[1]")
input("Press enter...")
dac3 = adafruit_mcp4725.MCP4725(tca[2], address=0x60)
print("connected to MCP on tca[2]")
input("Press enter...")
dac4 = adafruit_mcp4725.MCP4725(tca[3], address=0x60)
print("connected to MCP on tca[3]")
input("Press enter...")
dac5 = adafruit_mcp4725.MCP4725(tca[4], address=0x60)
print("connected to MCP on tca[4]")
# Optionally you can specify a different addres if you override the A0 pin.
# amp = adafruit_max9744.MAX9744(i2c, address=0x63)

# Three mode of setting DAC values
#using value with  16-bit number DAC resolution
#dac.value = 65535 # 0 (minimum/ground) to 65535 (maximum/Vout)
# using raw value with 12-bit DAC resolution
#dac.raw_value = 4095 # 0 (minimum/ground) to 4095 (maximum/Vout).
# using normalized_value
#dac.normalized_value = 1.0  #  0 (minimum/ground) to 1.0 (maximum/Vout).

dac1.normalized_value = 0.1
print("test 0.1 normalised o/p in DAC1")
dac2.normalized_value = 0.2
print("test 0.2 normalised o/p in DAC2")
dac3.normalized_value = 0.3
print("test 0.3 normalised o/p in DAC3")
dac4.normalized_value = 0.4
print("test 0.4 normalised o/p in DAC4")
dac5.normalized_value = 0.5
print("test 0.5 normalised o/p in DAC5")

input("press enter to exit..")
dac1.normalized_value = 0.0
dac2.normalized_value = 0.0
dac3.normalized_value = 0.0
dac4.normalized_value = 0.0
dac5.normalized_value = 0.0
GPIO.cleanup()

