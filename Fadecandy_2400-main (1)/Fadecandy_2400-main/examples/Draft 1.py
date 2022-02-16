import opc
import time
import random

leds = [(255,255,255)]*360 #white

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

#for led in leds: # pick out an element: led = (255,255,255)
for led in range(60): #pick out indeces: led = 0,1,2,3...
    
    h =[(0,0),(0,4),(1,0),(1,4)]
    time.sleep(1)
    client.put_pixels(leds)
    

