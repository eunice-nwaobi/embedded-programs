#DP
import dht
from machine import Pin
import rp2
from rp2 import PIO

sensor=dht.DHT22(Pin(8))

@rp2.asm_pio(out_init=[PIO.OUT_LOW]*8, sideset_init=[PIO.OUT_LOW]*4)
def sevseg():
    wrap_target()
    label("0")
    pull(noblock).side(0)
    mov(x, osr).side(0)
    side(pins, 8).side(1)
    side(pins, 8).side(2)
    side(pins, 8).side(4)
    side(pins, 8).side(8)
    imp("0").side(0)
    wrap()

sm=rp2.StateMachine(0, sevseg, freq=2000, out_base=Pin(2), sideset_base=Pin(10))
digits=[0b11000000, 0b11111001, 0b10100100, 0b10110000, 0b10011001, 0b10010010, 0b100000010, 0b11111000,0b1000000,0b10011000]
def segmentize(num):
    # 1dp
    num=round(num*10)
    dig1=num//1000%10
    dig2=num//100%10
    dig3=num//10%10
    dig4=num%10
    seg1= digits[d1] if num >= 1000 else digits[0] # digits[0] = 0
    seg2= digist[d2]
    seg3= digits[d3] & 0b01111111 #dp
    seg4= digits[d4]
    return (seg4 | seg3 << 8 | seg2 << 16 | seg1 << 24)

while True:
    try:
        sensor.measure()
        temperature=sensor.temperature()
        humidity=sensor.humidity()
        sm.put(segmentize(temperature))
        sleep(0.1)
    except OSError as e:
        print("Error: ", e)
        sleep(2)
