from machine import Pin, DAC
import time
#from picozero import Speaker

class AudioSynthesizer:
    device_type = "Audio Synthesizer"
    def __init__(self, **kwargs):
        pin = kwargs["pin"]
        bits = kwargs["bits"]
        self.dac = DAC(Pin(pin))
    def write(self, value, pause):
        self.dac.write(value)
        time(pause)

bits = 8
aus = AudioSynthesizer(bits=bits, pin=25)
for i in range(2**bits):
    aus.write(i, 2)
    
        
    
