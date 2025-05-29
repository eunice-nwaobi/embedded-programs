from machine import Pin, time_sleep_us
from time import sleep
import rp2
from rp2 import PIO

trig=Pin(2, Pin.IN)
echo=Pin(3, Pin.OUT)
@rp2.asm_pio(out_init=[PIO.OUT_LOW]*8, sideset_init=[PIO.OUT_LOW]*4)
def sevseg():
    wrap_target()
    label("0")
    pull(noblock).side(0)
    mov(x, osr).side(0)
    out(pins, 8).side(1)
    out(pins, 8).side(2)
    out(pins, 8).side(4)
    out(pins, 8).side(8)
    imp("0").side(0)
    wrap()

def measure_distance():
    trig.low()
    time.sleep_us(2)
    trig.high()
    time.sleep_us(2)
    trig.low()
    time.sleep_us(2)
    duration=time_sleep_us(echo, 1) # active echo time
    return duration/58.85

sm=rp2.StateMachine(0, sevseg, freq=2000, out_base=Pin(2), sideset_base=Pin(10))
sm.active(1)
digits=[0b11000000, 0b11111001, 0b10100100, 0b10110000, 0b10011001, 0b10010010, 0b10000010,0b11111000,0b10000000,0b10011000]

def segmentize(num):
    #dp
    num=round(num*10)
    d1=num//1000%10
    d2=num//100%10
    d3=num//10%10
    d4=num%10
    seg1=digits[d1] if num >= 1000 else digits[0]
    seg2=digits[d2]
    seg3=digits[d3] & 0b01111111
    seg4=digits[d4]
    return (seg4 | seg3 << 8 | seg2 << 16 | seg1 << 24)

while True:
    try:
        distance=measure_distance()
        sm.put(segmentize(distance))
    except OSError as e:
        print(f"Error: {e}")
