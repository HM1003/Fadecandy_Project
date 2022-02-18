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

def rainbow(pixels, order): #Pixels and order defined in the rainbow function. 
        
        if order == 'asc': #Each pixel in the range will increase in order or decrease. 
            ran = range(360)
        elif order == 'desc':
            ran = reversed(range(360))
                
        for hue in ran: 
            rgb_fractional = colorsys.hsv_to_rgb(hue/360.0, s, v) #HSV to RGB colour system returns float between 0 and 1
            r_float, g_float, b_float = rgb_fractional[0], rgb_fractional[1], rgb_fractional[2] #Extract floating point numbers
            
            rgb = (r_float*255, g_float*255, b_float*255) #Makes the new correct tupel value for RGB

            for p in pixels:
                leds[p] = rgb #leds will display and send out each pixel 
                
            client.put_pixels(leds)

            time.sleep(0.005)#

choice = raw_input("Choose animation?\n1. Loading Snake\n2. Fading lines\n3. Light up row\n4. Light up each pixel\n5. Light random pixel\n6. Light up name\n")

if choice == '1':
        for led in enumerate(leds):     #Displays each pixel on the animation board one by one.
                leds[led[0]] = (64,224,208) #Turquoise
                time.sleep(0.1)
                client.put_pixels(leds)
                
elif choice == '2': #If choice 1 is not selected elif gives the option to select other choices.
        n = 0       
        while n < 6:
                     for colour in range(256): 
                             for led in range(60): 
                                     leds[60*n+led] = (238,232,170) #The 60 leds in eacn now is being animated followed by the next row by n+=1. #Beige colour
                             client.put_pixels(leds) 
                             time.sleep(0.01) 
                     n+=1 
        
elif choice == '3':
        rows = raw_input('Which row do you want to light up?(seperate with comma)') #The user can input which row to light up e.g 1,3,5
        rows = re.findall('\d+', rows)
        rows_map = map(int, rows) #Maps out each row as an integer from 0 to 5.
        rows_list = list(rows_map)
        pix = []
        for row in rows_list:
                if row > 5: #If the user selects above 5 the number is not recognised.
                        print('Number is too large')
                else:
                        for x in range(row*60, row*60 + 60): 
                                pix.append(x)
        rainbow(pix, 'asc')
        
elif choice == '4':
        pixels = [0,60,120,180,240, 300] #Column Values are defined in tuples.
        x = 0
        while x<60:
                rainbow(pixels, 'asc')
                rainbow(pixels, 'desc')
                x += 1
                pixels = [p+1 for p in pixels] #Each column is displayed one by one as defined in pixels = p+1.
                client.put_pixels(leds)


elif choice == '5':
        rainbow(range(360), 'asc') #Controls the whole animation board.     
        leds=[(0,0,0)]*360
        client.put_pixels(leds)
        pixel = [0]
        while True:
                pix = random.randint(0,359) #Displays random integers from 0 to 359. 
                pixel[0] = pix
                rainbow(pixel, 'asc')
                time.sleep(0.01)
                

elif choice == '6':
        
        HUMENDRA = [0,60,120,180,240,300,4,64,124,184,244,304,121,122, 123,
                    6,66,126,186,246,306,307,308,309,310,10,70,130,190, 250,
                    12,72,132,192,252,312,73,134,75,16,76,136,196,256, 316,
                    18,78,138,198,258,318,19,20,21,22,139,140,141,142,319,320,321,322,
                    24,84,144,204,264,324,85,146,207,268,29,89,149,209,269,329,
                    31,91,151,211,271,331,32,33,34,322,333,334,35,95,155,215,275,335,
                    37,97,157,217,277,337,38,39,40,41,158,159,160,161,101,219,280,341,
                    48,107,166,225,284,343,167,168,169,170,109,231,292,353] 

        #Tupels values for each letter 

        for x in HUMENDRA:
                leds[x] = (64,224,208) #Turquoise
                client.put_pixels(leds)



else:
        print("Option not recognised")
        

##        H = [0,60,120,180,240,300,4,64,124,184,244,304,121,122, 123]
##        U = [6,66,126,186,246,306,307,308,309,310,10,70,130,190, 250]
##        M = [12,72,132,192,252,312,73,134,75,16,76,136,196,256, 316]
##        E = [18,78,138,198,258,318,19,20,21,22,139,140,141,142,319,320,321,322]
##        N = [24,84,144,204,264,324,85,146,207,268,29,89,149,209,269,329]
##        D = [31,91,151,211,271,331,32,33,34,322,333,334,35,95,155,215,275,335]
##        R = [37,97,157,217,277,337,38,39,40,41,158,159,160,161,101,219,280,341]
##        A = [48,107,166,225,284,343,167,168,169,170,109,231,292,353]   

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

        


        
