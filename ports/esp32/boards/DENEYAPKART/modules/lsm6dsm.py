import deneyap
from machine import Pin, I2C

class LSM6DSM():

    # Temperature registers
    OUT_TEMP_L = 0x20
    OUT_TEMP_H = 0x21

    # Gyroscope registers
    OUTX_L_G = 0x22
    OUTX_H_G = 0x23
    OUTY_L_G = 0x24
    OUTY_H_G = 0x25
    OUTZ_L_G = 0x26
    OUTZ_H_G = 0x27

    # Accelerometer registers
    OUTX_L_XL = 0x28
    OUTX_H_XL = 0x29
    OUTY_L_XL = 0x2A
    OUTY_H_XL = 0x2B
    OUTZ_L_XL = 0x2C
    OUTZ_H_XL = 0x2D

    # Control registers
    CTRL1_XL = 0x10
    CTRL2_G = 0x11
    CTRL3_C = 0x12
    CTRL4_C = 0x13
    CTRL5_C = 0x14
    CTRL6_C = 0x15
    CTRL7_G = 0x16
    CTRL8_XL = 0x17
    CTRL9_XL = 0x18
    CTRL10_C = 0x19

    # Unused constants
    WHO_AM_I = 0x0F
    SCALE_FOR_2G = 0.001
    SCALE_FOR_4G = 0.002
    SCALE_FOR_8G = 0.004
    SCALE_FOR_16G = 0.008
    DIV_2G = 100
    DIV_4G = 200
    DIV_8G = 400
    DIV_16G = 1200
    SCALE_FOR_250_DPS = 0.00875
    SCALE_FOR_500_DPS = 0.0175
    SCALE_FOR_2000_DPS = 0.070
    DIV_250_DPS = 875
    DIV_500_DPS = 1750
    DIV_2000_DPS = 7000

    initial_reg_values = [0x70, 0x4c, 0x44, 0x0, 0x0,
                          0x0, 0x50, 0x0, 0x38, 0x38]
    initial_registers = ['CTRL1_XL', 'CTRL2_G', 'CTRL3_C', 'CTRL4_C', 'CTRL5_C',
                         'CTRL6_C', 'CTRL7_G', 'CTRL8_XL', 'CTRL9_XL', 'CTRL10_C']

    def __init__(self, addr = 0x6a):
        # Initializing the I2C bus object
        self.i2c = I2C(0, sda = Pin(deneyap.SDA), scl = Pin(deneyap.SCL), freq = 100000)
        self.addr = addr

    def detect(self):
        assert(ord(self.read_reg(self.WHO_AM_I, 1)) == 0x6A), "Identification register value \
                                                       is wrong! Pass 'detect=False' \
                                                       to setup() to disable the check."

    def setup(self, detect = True):
        if detect:
            self.detect()
        # Safety check
        assert(len(self.initial_reg_values) == len(self.initial_registers)), \
                "Number of initial registers is not equal to number of initial \
                 register values. Set 'lsm.initial_registers' properly!"
        # Writing initial values into registers
        for i, reg_name in enumerate(self.initial_registers):
            self.write_reg(getattr(self, reg_name), self.initial_reg_values[i])
        return True

    def make_16bit_value(self, vh, vl):
        v = (ord(vh) << 8) | ord(vl)

        if v > 32767:
            v = v - 65536

        return v

    def get_raw_temp_value(self):
        th = self.read_reg(self.OUT_TEMP_H, 1)
        tl = self.read_reg(self.OUT_TEMP_L, 1)
        t = self.make_16bit_value(th, tl)

        return t

    def get_temp_value_celcius(self):
        data = float(self.get_raw_temp_value() / 256)
        data += 25

        return data

    def get_temp_value_fahrenheit(self):
        data = float(self.get_raw_temp_value() / 256)
        data += 25
        data = (data * 9) / 5 + 32

        return data


    def get_raw_gyro_values(self):
        gxh = self.read_reg(self.OUTX_H_G, 1)
        gxl = self.read_reg(self.OUTX_L_G, 1)
        gx = self.make_16bit_value(gxh, gxl)

        gyh = self.read_reg(self.OUTY_H_G, 1)
        gyl = self.read_reg(self.OUTY_L_G, 1)
        gy = self.make_16bit_value(gyh, gyl)

        gzh = self.read_reg(self.OUTZ_H_G, 1)
        gzl = self.read_reg(self.OUTZ_L_G, 1)
        gz = self.make_16bit_value(gzh, gzl)

        return gx, gy, gz

    def get_gyro_values(self):
        gx_raw, gy_raw, gz_raw = self.get_raw_gyro_values()

        gx = float(gx_raw * self.SCALE_FOR_2000_DPS)
        gy = float(gy_raw * self.SCALE_FOR_2000_DPS)
        gz = float(gz_raw * self.SCALE_FOR_2000_DPS)

        return gx, gy, gz

    def get_raw_accel_values(self):
        axh = self.read_reg(self.OUTX_H_XL, 1)
        axl = self.read_reg(self.OUTX_L_XL, 1)
        ax = self.make_16bit_value(axh, axl)

        ayh = self.read_reg(self.OUTY_H_XL, 1)
        ayl = self.read_reg(self.OUTY_L_XL, 1)
        ay = self.make_16bit_value(ayh, ayl)

        #print("{}\t{}".format(hex(ayh), hex(ayl)))

        azh = self.read_reg(self.OUTZ_H_XL, 1)
        azl = self.read_reg(self.OUTZ_L_XL, 1)
        az = self.make_16bit_value(azh, azl)

        return ax, ay, az

    def get_accel_values(self):
        ax_raw, ay_raw, az_raw = self.get_raw_accel_values()

        ax = float(ax_raw * 0.061 * self.SCALE_FOR_2G)
        ay = float(ay_raw * 0.061 * self.SCALE_FOR_2G)
        az = float(az_raw * 0.061 * self.SCALE_FOR_2G)

        return ax, ay, az

    def write_reg(self, reg, val):
        return self.i2c.writeto_mem(self.addr, reg, bytearray([val]))

    def read_reg(self, reg, nbytes):
        return self.i2c.readfrom_mem(self.addr, reg, nbytes)