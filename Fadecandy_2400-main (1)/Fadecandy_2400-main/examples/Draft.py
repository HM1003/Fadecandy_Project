import opc
import time
import random

leds = [(255,255,255)]*360 #white

client = opc.Client('localhost:7890')
client.put_pixels(leds)

#for led in leds: # pick out an element: led = (255,255,255)
for led in range(60): #pick out indeces: led = 0,1,2,3...
    client.put_pixels(leds)
    
    leds[0] = (0,255,0)
    time.sleep(.1)
    
    leds[60] = (255,0,0)
    time.sleep(.1)
    
    leds[120] = (255,0,0)
    time.sleep(.1)
    
    leds[180] = (255,0,0)
    time.sleep(.1)
        
    leds[240] = (255,0,0)
    time.sleep(.1)

    leds[300] = (255,0,0)
    time.sleep(0.1)
#H line 

    leds[4] = (0,255,0)
    time.sleep(.1)
    
    leds[64] = (255,0,0)
    time.sleep(.1)
    
    leds[124] = (255,0,0)
    time.sleep(.1)
    
    leds[184] = (255,0,0)
    time.sleep(.1)
        
    leds[244] = (255,0,0)
    time.sleep(.1)

    leds[304] = (255,0,0)
    time.sleep(0.1)
#H line

    leds[121] = (255,0,0)
    time.sleep(.1)

    leds[122] = (255,0,0)
    time.sleep(.1)

    leds[123] = (255,0,0)
    time.sleep(.1)
#H bridge
    
    leds[6] = (0,255,0)
    time.sleep(.1)
    
    leds[66] = (255,0,0)
    time.sleep(.1)
    
    leds[126] = (255,0,0)
    time.sleep(.1)
    
    leds[186] = (255,0,0)
    time.sleep(.1)
        
    leds[246] = (255,0,0)
    time.sleep(.1)

    leds[306] = (255,0,0)
    time.sleep(0.1)

#U first line

    leds[307] = (255,0,0)
    time.sleep(0.1)
    
    leds[308] = (255,0,0)
    time.sleep(0.1)
    
    leds[309] = (255,0,0)
    time.sleep(0.1)
    
    leds[310] = (255,0,0)
    time.sleep(0.1)

#U bridge

    leds[10] = (0,255,0)
    time.sleep(.1)
    
    leds[70] = (255,0,255)
    time.sleep(.1)
    
    leds[130] = (255,0,255)
    time.sleep(.1)
    
    leds[190] = (255,0,0)
    time.sleep(.1)
        
    leds[250] = (255,0,0)
    time.sleep(.1)
#U second line

    leds[12] = (0,255,0)
    time.sleep(.1)
    
    leds[72] = (255,0,0)
    time.sleep(.1)
    
    leds[132] = (255,0,0)
    time.sleep(.1)
    
    leds[192] = (255,0,0)
    time.sleep(.1)
        
    leds[252] = (255,0,0)
    time.sleep(.1)

    leds[312] = (255,0,0)
    time.sleep(0.1)
#M first line

    leds[73] = (255,0,0)
    time.sleep(.1)

    leds[134] = (255,0,0)
    time.sleep(.1)

    leds[75] = (255,0,0)
    time.sleep(.1)

#M bridge
    
    leds[16] = (0,255,0)
    time.sleep(.1)

    leds[76] = (255,0,0)
    time.sleep(.1)
    
    leds[136] = (255,0,0)
    time.sleep(.1)
    
    leds[196] = (255,0,0)
    time.sleep(.1)
        
    leds[256] = (255,0,0)
    time.sleep(.1)

    leds[316] = (255,0,0)
    time.sleep(0.1)
#M second line

    leds[18] = (0,255,0)
    time.sleep(.1)

    leds[78] = (255,0,0)
    time.sleep(.1)
    
    leds[138] = (255,0,0)
    time.sleep(.1)
    
    leds[198] = (255,0,0)
    time.sleep(.1)
        
    leds[258] = (255,0,0)
    time.sleep(.1)

    leds[318] = (255,0,0)
    time.sleep(0.1)

#E first line

    leds[19] = (0,255,0)
    time.sleep(.1)

    leds[20] = (0,255,0)
    time.sleep(.1)

    leds[21] = (0,255,0)
    time.sleep(.1)

    leds[22] = (0,255,0)
    time.sleep(.1)

    leds[139] = (255,0,0)
    time.sleep(.1)

    leds[140] = (255,0,0)
    time.sleep(.1)

    leds[141] = (255,0,0)
    time.sleep(.1)

    leds[142] = (255,0,0)
    time.sleep(.1)

    leds[319] = (255,0,0)
    time.sleep(0.1)

    leds[320] = (255,0,0)
    time.sleep(0.1)

    leds[321] = (255,0,0)
    time.sleep(0.1)

    leds[322] = (255,0,0)
    time.sleep(0.1)

#E bridge

    
