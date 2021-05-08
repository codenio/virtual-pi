import numpy as np

class I2C:
    def __init__(self, scl, sda, frequency=400000):
        print(f"I2C confifure using SCL: {scl}, SDA: {sda}, at freq: {frequency}")

    def scan(self):
        return list(np.random.randint(255, size=(np.random.choice([1,2]))))
