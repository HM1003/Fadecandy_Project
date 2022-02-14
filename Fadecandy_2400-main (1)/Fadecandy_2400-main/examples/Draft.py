import opc
import time
import random

leds = [(255,255,255)]*360 #white

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

#for led in leds: # pick out an element: led = (255,255,255)
for led in range(60): #pick out indeces: led = 0,1,2,3...
    leds[300] = (255,0,0)
    time.sleep(1)
    client.put_pixels(leds)

    leds[0] = (0,255,0)
    time.sleep(.1)
    client.put_pixels(leds)

    leds[60] = (255,0,0)
    time.sleep(.1)
    client.put_pixels(leds)

    leds[120] = (255,0,0)
    time.sleep(.1)
    client.put_pixels(leds)

    leds[180] = (255,0,0)
    time.sleep(.1)
    client.put_pixels(leds)
    
    leds[240] = (255,0,0)
    time.sleep(.1)
    client.put_pixels(leds)

h=[(0,0),(0,4),(1,0),(1,4)]

