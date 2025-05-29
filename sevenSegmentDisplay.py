#7-segment display
from machine import Pin
from time import sleep

pins1=[(2, machine.Pin.OUT), #A
       (3, machine.Pin.OUT), #B
       (4, machine.Pin.OUT), #C
       (5, machine.Pin.OUT), #D
       (6, machine.Pin.OUT), #E
       (7, machine.Pin.OUT), #F
       (8, machine.Pin.OUT), #G
       (0, machine.Pin.OUT) #DP
       ]
pins2=[(9, machine.Pin.OUT), #A
       (10, machine.Pin.OUT), #B
       (11, machine.Pin.OUT), #C
       (12, machine.Pin.OUT), #D
       (13, machine.Pin.OUT), #E
       (14, machine.Pin.OUT), #F
       (15, machine.Pin.OUT), #G
       (1, machine.Pin.OUT) #DP
       ]
 
digits=[[0,0,0,0,0,0,1,1], #0,
        [1,0,0,1,1,1,1,1], #1
        [0,0,1,0,0,1,0,1], #2
        [0,0,0,0,1,1,0,1], #3
        [1,0,0,1,1,0,0,1], #4
        [0,1,0,0,1,0,0,1], #5
        [0,1,0,0,0,0,0,1], #6
        [0,0,0,1,1,1,1,1], #7
        [0,0,0,0,0,0,0,1], #8
        [0,0,0,1,1,0,0,1], #9
        [0,0,0,1,0,0,0,1], #A
        [1,1,0,0,0,0,0,1], #b
        [0,1,1,0,0,0,1,1], #C
        [1,0,0,0,0,1,0,1], #d
        [0,1,1,0,0,0,0,1], #E
        [0,1,1,1,0,0,0,1] #F
        ]

def reset():
    for pin in pins1:
        pins1.value(1)
    for pin in pins2:
        pins2.value(1)
reset()

switch = Pin(13, Pin.IN, Pin.PULL_UP)

while True:
    if switch.value() == 1:
        for i in range(len(digits)):
            if switch.value() == 0:
                break
        for j in range(len(pins1)-1):
            pins1[j].value(digits[i][j])
            pins2[j].value(digits[len(digits)-1-i][j])
        sleep(0.5)
    else:
        for i in range(len(digits)-1, -1, -1):
            if switch.value()==1:
                break
        for j in range(len(pins1)):
            pins1[j].value(digits[i][j])
            pins2[j].value(digits[len(digits)-1-i][j])
        sleep(0.5)
    
