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

    leds[24] = (0,255,0)
    time.sleep(.1)

    leds[84] = (255,0,0)
    time.sleep(.1)
    
    leds[144] = (255,0,0)
    time.sleep(.1)
    
    leds[204] = (255,0,0)
    time.sleep(.1)
        
    leds[264] = (255,0,0)
    time.sleep(.1)

    leds[324] = (255,0,0)
    time.sleep(0.1)
    
# N first line

    leds[85] = (255,0,0)
    time.sleep(.1)
    
    leds[146] = (255,0,0)
    time.sleep(.1)
    
    leds[207] = (255,0,0)
    time.sleep(.1)
        
    leds[268] = (255,0,0)
    time.sleep(.1)

#N bridge
    
    leds[29] = (0,255,0)
    time.sleep(.1)

    leds[89] = (255,0,0)
    time.sleep(.1)
    
    leds[149] = (255,0,0)
    time.sleep(.1)
    
    leds[209] = (255,0,0)
    time.sleep(.1)
        
    leds[269] = (255,0,0)
    time.sleep(.1)

    leds[329] = (255,0,0)
    time.sleep(0.1)

#N second line

    leds[31] = (0,255,0)
    time.sleep(.1)

    leds[91] = (255,0,0)
    time.sleep(.1)
    
    leds[151] = (255,0,0)
    time.sleep(.1)
    
    leds[211] = (255,0,0)
    time.sleep(.1)
        
    leds[271] = (255,0,0)
    time.sleep(.1)

    leds[331] = (255,0,0)
    time.sleep(0.1)
    
#D first line

    leds[32] = (0,255,0)
    time.sleep(.1)

    leds[33] = (0,255,0)
    time.sleep(.1)

    leds[34] = (0,255,0)
    time.sleep(.1)

    leds[332] = (255,0,0)
    time.sleep(0.1)

    leds[333] = (255,0,0)
    time.sleep(0.1)

    leds[334] = (255,0,0)
    time.sleep(0.1)

#D bridge    

    leds[35] = (0,255,0)
    time.sleep(.1)

    leds[95] = (255,0,0)
    time.sleep(.1)
    
    leds[155] = (255,0,0)
    time.sleep(.1)
    
    leds[215] = (255,0,0)
    time.sleep(.1)
        
    leds[275] = (255,0,0)
    time.sleep(.1)

    leds[335] = (255,0,0)
    time.sleep(0.1)
    
#D second line

    leds[37] = (0,255,0)
    time.sleep(.1)

    leds[97] = (255,0,0)
    time.sleep(.1)
    
    leds[157] = (255,0,0)
    time.sleep(.1)
    
    leds[217] = (255,0,0)
    time.sleep(.1)
        
    leds[277] = (255,0,0)
    time.sleep(.1)

    leds[337] = (255,0,0)
    time.sleep(0.1)

#R first line

    leds[38] = (0,255,0)
    time.sleep(.1)

    leds[39] = (0,255,0)
    time.sleep(.1)

    leds[40] = (0,255,0)
    time.sleep(.1)

    leds[41] = (0,255,0)
    time.sleep(.1)

    leds[158] = (255,0,0)
    time.sleep(.1)

    leds[159] = (255,0,0)
    time.sleep(.1)

    leds[160] = (255,0,0)
    time.sleep(.1)

    leds[161] = (255,0,0)
    time.sleep(.1)

    leds[101] = (255,0,0)
    time.sleep(.1)

    leds[219] = (255,0,0)
    time.sleep(.1)
        
    leds[280] = (255,0,0)
    time.sleep(.1)

    leds[341] = (255,0,0)
    time.sleep(0.1)
    
#R bridge

    leds[48] = (0,255,0)
    time.sleep(.1)

    leds[107] = (255,0,0)
    time.sleep(.1)
    
    leds[166] = (255,0,0)
    time.sleep(.1)
    
    leds[225] = (255,0,0)
    time.sleep(.1)
        
    leds[284] = (255,0,0)
    time.sleep(.1)

    leds[343] = (255,0,0)
    time.sleep(0.1)

#A first line

    leds[167] = (255,0,0)
    time.sleep(.1)

    leds[168] = (255,0,0)
    time.sleep(.1)

    leds[169] = (255,0,0)
    time.sleep(.1)

    leds[170] = (255,0,0)
    time.sleep(.1)

#A bridge

    leds[109] = (255,0,0)
    time.sleep(.1)

    leds[231] = (255,0,0)
    time.sleep(.1)
        
    leds[292] = (255,0,0)
    time.sleep(.1)

    leds[353] = (255,0,0)
    time.sleep(0.1)

#A second line

    

    
