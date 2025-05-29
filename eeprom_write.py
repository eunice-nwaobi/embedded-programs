from machine import I2C, Pin
EEPROM_address = 0x50
i2c=I2C(0, scl=Pin(22), sda=Pin(21), freq=1000000)
def write_EEPROM(address, data):
    data=bytes([address]) + data.encode() #bytes address followed by encoding
    i2c.writeto(EEPROM_address, data)
write_EEPROM(0x00, "Hello")

from machine import I2C,Pin
EEPROM_address = 0x50
i2c=I2C(0, freq=1000000, scl=Pin(22), sda=Pin(21))
def write_EEPROM(address, data):
    data = bytes([address]) + data.encode()
    i2c.writeto(EEPROM_address, data)
    return i2c.writeto(EEPROM_ADDRESS, data)


import ssd1306
from machine import Pin, SPI
spi=SPI(0, baudrate=1000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
cs=Pin(5, Pin.OUT)
ds=Pin(16)
rst=Pin(17)
oled=ssd1306.SSD1306(128, 64, spi, ds, rst, cs)
oled.text("Hello", 0,0)
oled.show()#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
