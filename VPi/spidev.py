class SpiDev:

    bits_per_word = 8
    cshigh = False
    loop = False
    lsbfirst = False
    max_speed_hz = 125000000
    mode = 0
    threewire = False
    no_cs = False

    def __init__(self, bus=0, cs=0):
        print(f"Opened SPI device on bus : {bus} with cs : {cs}")

    def open(self, bus, cs):
        print(f"Opened SPI device on bus : {bus} with cs : {cs}")

    def close(self):
        print("Closed SPI")

    def fileno(self):
        pass

    def readbytes(self, length):
        return list(np.random.rand(length)*255)

    def writebytes(self,values):
        print(f"writebytes : {values}")

    def writebytes2(self,values):
        print(f"writebytes2 : {values}")

    def xfer(self, values, speed=4096, delay=0, bits=8):
        print(f"xfer : {values} at speed : {speed} with delay : {delay} using bits : {bits}")

    def xfer2(self, values, speed=4096, delay=0, bits=8):
        print(f"xfer2 : {values} at speed : {speed} with delay : {delay} using bits : {bits}")

    def xfer3(self, values, speed=4096, delay=0, bits=8):
        print(f"xfer2 : {values} at speed : {speed} with delay : {delay} using bits : {bits}")
