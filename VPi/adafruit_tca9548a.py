# # The MIT License (MIT)
# #
# # Copyright (c) 2018 Carter Nelson for Adafruit Industries
# #
# # Permission is hereby granted, free of charge, to any person obtaining a copy
# # of this software and associated documentation files (the "Software"), to deal
# # in the Software without restriction, including without limitation the rights
# # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# # copies of the Software, and to permit persons to whom the Software is
# # furnished to do so, subject to the following conditions:
# #
# # The above copyright notice and this permission notice shall be included in
# # all copies or substantial portions of the Software.
# #
# # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# # THE SOFTWARE.
# """
# ``Adafruit_TCA9548A``
# ====================================================
#
# CircuitPython driver for the TCA9548A I2C Multiplexer.
#
# * Author(s): Carter Nelson
#
# Implementation Notes
# --------------------
#
# **Hardware:**
#
# * TCA9548A I2C Multiplexer: https://www.adafruit.com/product/2717
#
# **Software and Dependencies:**
#
# * Adafruit CircuitPython firmware for the supported boards:
#   https://github.com/adafruit/circuitpython/releases
# * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
# """
#
# # imports
import time
import numpy as np
# from micropython import const

_DEFAULT_ADDRESS = 0x70

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_TCA9548A.git"


class TCA9548A_Channel:
    """Helper class to represent an output channel on the TCA9548A and take care
       of the necessary I2C commands for channel switching. This class needs to
       behave like an I2CDevice."""

    def __init__(self, tca, channel):
        self.tca = tca
        self.channel_switch = bytearray([1 << channel])

    def scan(self):
        return list(np.random.randint(255, size=(np.random.choice([1,2,3])))) + [_DEFAULT_ADDRESS]

class TCA9548A:
    """Class which provides interface to TCA9548A I2C multiplexer."""
    def __init__(self, i2c, address=_DEFAULT_ADDRESS):
        self.i2c = i2c
        self.address = address
        self.channels = [None] * 8

    def __len__(self):
        return 8

    def __getitem__(self, key):
        if not 0 <= key <= 7:
            raise IndexError("Channel must be an integer in the range: 0-7")
        if self.channels[key] is None:
            self.channels[key] = TCA9548A_Channel(self, key)
        return self.channels[key]
