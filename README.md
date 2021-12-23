# virtual-pi
Virtual Pi Library for mocking Raspberry Pi

VPi is a python library that supports development of software/program and to debug them outside RPi (eg: ubuntu ). it can be intergrated along with any generic application/program/software.

it help in making your program/application run seamlessly both outside and inside RPi by

- Printing the intended actions (without GUI) for debugging, when executed outside RPi
- Works exactly as intended in an actual RPi without a need for code change.

To use the mock or virtual pi just type the following at the beginning of your script.

The easiest way to use this package is to install using pip3 for python 3

```bash
$ sudo pip3 install VPi
```

## Works with

- [python 3.6.8](https://www.python.org/downloads/release/3.6.8)


### Sub Modules:

- board

	This Libary simulates pin of the raspberry pi based on the board type

- busio

	This Libary simulates I2C communication

- spidev

	This Libary simulates SPI communication by mocking py-spidev library

- GPIO

	This library simulates the following functions which are used in the RPi.GPIO library.
	- GPIO.setmode()
	- GPIO.getmode()
	- GPIO.setwarnings()
	- GPIO.setup()
	- GPIO.output()
	- GPIO.input()
	- GPIO.wait_for_edge()
	- GPIO.add_event_detect()
	- GPIO.event_detected()
	- GPIO.add_event_callback()
	- GPIO.remove_event_detect()
	- GPIO.gpio_function()
	- GPIO.start()
	- GPIO.ChangeFrequency()
	- GPIO.ChangeDutyCycle()
	- GPIO.stop()
	- GPIO.cleanup()

- adafruit_mcp4725

	This library simulates the MCP4725 DAC ic using adafruit_mcp4725

- adafruit_tca9548a

	This library simulates the TCA9548A I2C Mux ic using adafruit_tca9548a


### Usage:

To use the mock or virtual pi just type the following at the beginning of your script.

```python
try:
	from RPi.GPIO import GPIO
	import board
	import busio
except:
	from VPi.GPIO import GPIO
	import VPi.board as board
	import VPi.busio as busio
```
### Example:

- [GPIO](example/GPIO-test.py)

	The following python example/test.py
	```python
	try:
	    import RPi.GPIO as GPIO
	except:
	    import VPi.GPIO as GPIO
	import time
	print ("set mode")
	GPIO.setmode(GPIO.BCM)
	print ("set warning false")
	GPIO.setwarnings(False)
	GPIO.setup(15,GPIO.OUT)
	GPIO.output(15,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(15,GPIO.LOW)
	```
	generates following output
	```shell
	$ export LOG_LEVEL=Info
	$ python examples/test.py
	set mode
	set warning false
	2020-05-07 17:49:23,031:INFO: Set Warings as False
	2020-05-07 17:49:23,031:INFO: setup channel : 15 as 0 with intial :0 and pull_up_dowm 20
	2020-05-07 17:49:23,032:INFO: output channel : 15 with value : 1
	2020-05-07 17:49:24,033:INFO: output channel : 15 with value : 0
	```


- [adafruit_mcp4725](example/mcp4725-test.py)

	Helps in seamless switching of enviroments

	```python
	try:
	    import RPi.GPIO as GPIO
	    import board
	    import busio
	    import adafruit_mcp4725
	except:
	    import VPi.GPIO as GPIO
	    import VPi.board as board
	    import VPi.busio as busio
	    import VPi.adafruit_mcp4725 as adafruit_mcp4725
	```

- [adafruit_tca9548a](example/tca9548a-test.py)

	Helps in seamless switching of enviroments

	```python
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

	```


## Develope

- make the suitable changes and from the root directory of this repository, install the VPi python package using the install.sh script
    ```bash
    $ sudo ./scripts/install.sh
    ```

## Contribute

- You've discovered a bug or something else you want to change - excellent! - feel free to raise a issue.
- You've worked out a way to fix it – even better! - submit your PR
- You want to tell us about it – best of all!

Start contributing !

## CREDITS

- [adafruit](https://github.com/adafruit)
