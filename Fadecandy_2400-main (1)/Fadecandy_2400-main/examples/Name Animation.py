import opc
import time
import random
import colorsys
import re

leds = [(0,0,0)]*360 #background color

s = 1.0 #Maximum colour
v = 1.0 #Maximum brightness

client = opc.Client('localhost:7890') # host
client.put_pixels(leds)

def rainbow(pixels, order):
        if order == 'asc':
            ran == range(360)
        elif order == 'desc':
            ran = reversed(range(360))
                
        for hue in ran:
            rgb_fractional = colorsys.hsv_to_rgb(hue/360.0, s, v) #
            
##for led in range(60): #picking out location of leds from column and rows. 
##    client.put_pixels(leds)
##    
##    leds[0] = (0,255,0) #RGB sequence (Red,Green,Blue) with a maximum brightness of 255.
##    time.sleep(.1) #10ms delay
##    
##    leds[60] = (0,255,0) #Pixel from led matrix value is 60, this location is specified as leds[60].
##    time.sleep(.1)
##    
##    leds[120] = (0,255,0)
##    time.sleep(.1)
##    
##    leds[180] = (0,255,0)
##    time.sleep(.1)
##        
##    leds[240] = (0,255,0)
##    time.sleep(.1)
##
##    leds[300] = (0,255,0)
##    time.sleep(0.1)
##    
###H first line. Above is the values to create the first part of the letter H.
##
##    leds[4] = (0,255,0)
##    time.sleep(.1)
##    
##    leds[64] = (0,255,0)
##    time.sleep(.1)
##    
##    leds[124] = (0,255,0)
##    time.sleep(.1)
##    
##    leds[184] = (0,255,0)
##    time.sleep(.1)
##        
##    leds[244] = (0,255,0)
##    time.sleep(.1)
##
##    leds[304] = (0,255,0)
##    time.sleep(0.1)
##    
###H second line. As all the lines in this value are from the 4th comumn, it is easier to group the location.
##
##    leds[121] = (0,255,0)
##    time.sleep(.1)
##
##    leds[122] = (0,255,0)
##    time.sleep(.1)
##
##    leds[123] = (0,255,0)
##    time.sleep(.1)
##    
###H bridge. By grouping the letter into sections it is easier to modify the value and connect more letters. 
##    
##    leds[6] = (255,255,0) #Using colors red and green to make yellow.
##    time.sleep(.1)
##    
##    leds[66] = (255,255,0)
##    time.sleep(.1)
##    
##    leds[126] = (255,255,0)
##    time.sleep(.1)
##    
##    leds[186] = (255,255,0)
##    time.sleep(.1)
##        
##    leds[246] = (255,255,0)
##    time.sleep(.1)
##
##    leds[306] = (255,255,0)
##    time.sleep(0.1)
##
###U first line
##
##    leds[307] = (255,255,0)
##    time.sleep(0.1)
##    
##    leds[308] = (255,255,0)
##    time.sleep(0.1)
##    
##    leds[309] = (255,255,0)
##    time.sleep(0.1)
##    
##    leds[310] = (255,255,0)
##    time.sleep(0.1)
##
###U bridge
##
##    leds[10] = (255,255,0)
##    time.sleep(.1)
##    
##    leds[70] = (255,255,0)
##    time.sleep(.1)
##    
##    leds[130] = (255,255,0)
##    time.sleep(.1)
##    
##    leds[190] = (255,255,0)
##    time.sleep(.1)
##        
##    leds[250] = (255,255,0)
##    time.sleep(.1)
###U second line
##
##    leds[12] = (0,0,255) #Blue colour for letter M
##    time.sleep(.1)
##    
##    leds[72] = (0,0,255)
##    time.sleep(.1)
##    
##    leds[132] = (0,0,255)
##    time.sleep(.1)
##    
##    leds[192] = (0,0,255)
##    time.sleep(.1)
##        
##    leds[252] = (0,0,255)
##    time.sleep(.1)
##
##    leds[312] = (0,0,255)
##    time.sleep(0.1)
###M first line
##
##    leds[73] = (0,0,255)
##    time.sleep(.1)
##
##    leds[134] = (0,0,255)
##    time.sleep(.1)
##
##    leds[75] = (0,0,255)
##    time.sleep(.1)
##
###M bridge
##    
##    leds[16] = (0,0,255)
##    time.sleep(.1)
##
##    leds[76] = (0,0,255)
##    time.sleep(.1)
##    
##    leds[136] = (0,0,255)
##    time.sleep(.1)
##    
##    leds[196] = (0,0,255)
##    time.sleep(.1)
##        
##    leds[256] = (0,0,255)
##    time.sleep(.1)
##
##    leds[316] = (0,0,255)
##    time.sleep(0.1)
###M second line
##
##    leds[18] = (255,165,0) #Mixing red and green to make the colour orange for letter E
##    time.sleep(.1)
##
##    leds[78] = (255,165,0)
##    time.sleep(.1)
##    
##    leds[138] = (255,165,0)
##    time.sleep(.1)
##    
##    leds[198] = (255,165,0)
##    time.sleep(.1)
##        
##    leds[258] = (255,165,0)
##    time.sleep(.1)
##
##    leds[318] = (255,165,0)
##    time.sleep(0.1)
##
###E first line
##
##    leds[19] = (255,165,0)
##    time.sleep(.1)
##
##    leds[20] = (255,165,0)
##    time.sleep(.1)
##
##    leds[21] = (255,165,0)
##    time.sleep(.1)
##
##    leds[22] = (255,165,0)
##    time.sleep(.1)
##
##    leds[139] = (255,165,0)
##    time.sleep(.1)
##
##    leds[140] = (255,165,0)
##    time.sleep(.1)
##
##    leds[141] = (255,165,0)
##    time.sleep(.1)
##
##    leds[142] = (255,165,0)
##    time.sleep(.1)
##
##    leds[319] = (255,165,0)
##    time.sleep(0.1)
##
##    leds[320] = (255,165,0)
##    time.sleep(0.1)
##
##    leds[321] = (255,165,0)
##    time.sleep(0.1)
##
##    leds[322] = (255,165,0)
##    time.sleep(0.1)
##
###E bridge
##
##    leds[24] = (255,0,0)
##    time.sleep(.1)
##
##    leds[84] = (255,0,0)
##    time.sleep(.1)
##    
##    leds[144] = (255,0,0)
##    time.sleep(.1)
##    
##    leds[204] = (255,0,0)
##    time.sleep(.1)
##        
##    leds[264] = (255,0,0)
##    time.sleep(.1)
##
##    leds[324] = (255,0,0)
##    time.sleep(0.1)
##    
### N first line
##
##    leds[85] = (255,0,0) #Red colour for letter N
##    time.sleep(.1)
##    
##    leds[146] = (255,0,0)
##    time.sleep(.1)
##    
##    leds[207] = (255,0,0)
##    time.sleep(.1)
##        
##    leds[268] = (255,0,0)
##    time.sleep(.1)
##
###N bridge
##    
##    leds[29] = (255,0,0)
##    time.sleep(.1)
##
##    leds[89] = (255,0,0)
##    time.sleep(.1)
##    
##    leds[149] = (255,0,0)
##    time.sleep(.1)
##    
##    leds[209] = (255,0,0)
##    time.sleep(.1)
##        
##    leds[269] = (255,0,0)
##    time.sleep(.1)
##
##    leds[329] = (255,0,0)
##    time.sleep(0.1)
##
###N second line
##
##    leds[31] = (64,224,208) #Mixing R,G,B to make letter D turquoise.
##    time.sleep(.1)
##
##    leds[91] = (64,224,208)
##    time.sleep(.1)
##    
##    leds[151] = (64,224,208)
##    time.sleep(.1)
##    
##    leds[211] = (64,224,208)
##    time.sleep(.1)
##        
##    leds[271] = (64,224,208)
##    time.sleep(.1)
##
##    leds[331] = (64,224,208)
##    time.sleep(0.1)
##    
###D first line
##
##    leds[32] = (64,224,208)
##    time.sleep(.1)
##
##    leds[33] = (64,224,208)
##    time.sleep(.1)
##
##    leds[34] = (64,224,208)
##    time.sleep(.1)
##
##    leds[332] = (64,224,208)
##    time.sleep(0.1)
##
##    leds[333] = (64,224,208)
##    time.sleep(0.1)
##
##    leds[334] = (64,224,208)
##    time.sleep(0.1)
##
###D bridge    
##
##    leds[35] = (64,224,208)
##    time.sleep(.1)
##
##    leds[95] = (64,224,208)
##    time.sleep(.1)
##    
##    leds[155] = (64,224,208)
##    time.sleep(.1)
##    
##    leds[215] = (64,224,208)
##    time.sleep(.1)
##        
##    leds[275] = (64,224,208)
##    time.sleep(.1)
##
##    leds[335] = (64,224,208)
##    time.sleep(0.1)
##    
###D second line
##
##    leds[37] = (245,245,220)    # Mixing R,G,B to make colour Beige for Letter R
##    time.sleep(.1)
##
##    leds[97] = (245,245,220)
##    time.sleep(.1)
##    
##    leds[157] = (245,245,220)
##    time.sleep(.1)
##    
##    leds[217] = (245,245,220)
##    time.sleep(.1)
##        
##    leds[277] = (245,245,220)
##    time.sleep(.1)
##
##    leds[337] = (245,245,220)
##    time.sleep(0.1)
##
###R first line
##
##    leds[38] = (245,245,220)    
##    time.sleep(.1)
##
##    leds[39] = (245,245,220)
##    time.sleep(.1)
##
##    leds[40] = (245,245,220)
##    time.sleep(.1)
##
##    leds[41] = (245,245,220)
##    time.sleep(.1)
##
##    leds[158] = (245,245,220)
##    time.sleep(.1)
##
##    leds[159] = (245,245,220)
##    time.sleep(.1)
##
##    leds[160] = (245,245,220)
##    time.sleep(.1)
##
##    leds[161] = (245,245,220)
##    time.sleep(.1)
##
##    leds[101] = (245,245,220)
##    time.sleep(.1)
##
##    leds[219] = (245,245,220)
##    time.sleep(.1)
##        
##    leds[280] = (245,245,220)
##    time.sleep(.1)
##
##    leds[341] = (245,245,220)
##    time.sleep(0.1)
##    
###R bridge
##
##    leds[48] = (238,232,170) #Mixing R,G,B to make colour Gold for letter A
##    time.sleep(.1)
##
##    leds[107] = (238,232,170)
##    time.sleep(.1)
##    
##    leds[166] = (238,232,170)
##    time.sleep(.1)
##    
##    leds[225] = (238,232,170)
##    time.sleep(.1)
##        
##    leds[284] = (238,232,170)
##    time.sleep(.1)
##
##    leds[343] = (238,232,170)
##    time.sleep(0.1)
##
###A first line
##
##    leds[167] = (238,232,170)
##    time.sleep(.1)
##
##    leds[168] = (238,232,170)
##    time.sleep(.1)
##
##    leds[169] = (238,232,170)
##    time.sleep(.1)
##
##    leds[170] = (238,232,170)
##    time.sleep(.1)
##
###A bridge
##
##    leds[109] = (238,232,170)
##    time.sleep(.1)
##
##    leds[231] = (238,232,170)
##    time.sleep(.1)
##        
##    leds[292] = (238,232,170)
##    time.sleep(.1)
##
##    leds[353] = (238,232,170)
##    time.sleep(0.1)
##
###A second line
##
##    

    

