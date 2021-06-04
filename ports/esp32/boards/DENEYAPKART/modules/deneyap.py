# Deneyap Kart MicroPython Helper Library
# 2021 May, Ozgur BOSTAN @RFtek Electronics Ltd.
#

# Import required libraries
from micropython import const
from machine import Pin
      
# Deneyap Kart Hardware Pin Assignments

# Digital pins
D0 = const(23)
D1 = const(22)
D2 = const(1)
D3 = const(3)
D4 = const(21)
D5 = const(19)
D6 = const(18)
D7 = const(5)
D8 = const(0)
D9 = const(2)
D10 = const(4)
D11 = const(15)
D12 = const(13)
D13 = const(12)
D14 = const(14)
D15 = const(27)

# Analog input pins
A0 = const(36)
A1 = const(39)
A2 = const(34)
A3 = const(35)
A4 = const(32)
A5 = const(33)

# Analog output pins
DAC1 = const(25)
DAC2 = const(26)

# I2C pins
SDA = const(4)
SCL = const(15)

# SPI pins
MOSI = const(5)
SCK = const(19)
MISO = const(18)

# UART pins
TX = const(1)
RX = const(3)

# PWM pins
PWM0 = const(23)
PWM1 = const(22)

# Microphone pins
MICD = const(12)
MICC = const(13)

# IMU pins
IMUSD = const(4)               
IMUSC = const(15)             

# Camera pins
CAMSD = const(33)         
CAMSC = const(25)         
CAMD2 = const(19)         
CAMD3 = const(22)         
CAMD4 = const(23)         
CAMD5 = const(21)         
CAMD6 = const(18)         
CAMD7 = const(26)         
CAMD8 = const(35)         
CAMD9 = const(34)         
CAMPC = const(5)         
CAMXC = const(32)         
CAMH = const(39)       
CAMV = const(36)       

# Built-in leds and button
LEDR = const(3)
LEDG = const(1)
LEDB = const(4)
GPKEY = const(0)

# Helper functions

# Change built-in red led (RGB) state 
def setRedLed(state):
    Pin(LEDR, Pin.OUT)

    if state:
        Pin(LEDR).value(0)
    else:
        Pin(LEDR).value(1)

# Change built-in green led (RGB) state 
def setGreenLed(state):
    Pin(LEDG, Pin.OUT)

    if state:
        Pin(LEDG).value(0)
    else:
        Pin(LEDG).value(1)

# Change built-in blue led (RGB) state 
def setBlueLed(state):
    Pin(LEDB, Pin.OUT)

    if state:
        Pin(LEDB).value(0)
    else:
        Pin(LEDB).value(1)

# Read built-in general purpose button state
def readGpKey():
    Pin(GPKEY, Pin.IN)

    return Pin(GPKEY).value()