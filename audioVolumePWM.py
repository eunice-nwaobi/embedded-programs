from machine import PWM, Pin
from time import sleep

class AudioVolume:
    device_type = "Audio Volume"
    def __init__(self, **kwargs):
        pin = kwargs["pin"]
        bits = kwargs["bits"]
        freq = kwargs["freq"]
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(freq)
        self.pwm.duty(2**bits)

    def adjustVolume(self, value):
        self.pwm.duty(value)
        sleep(2)

bits = 10
aux = AudioVolume(pin=15, bits=bits, freq=1000)
while True:
    for i in range(0, 2**bits, 10):
        aux.adjustVolume(i)

    for j in range(2**bits-1, 0, -10):
        aux.adjustVolume(j)
