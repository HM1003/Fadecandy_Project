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

            time.sleep(0.01)#10ms

choice = raw_input("Choose animation?\n1. Loading Snake\n2. Fading Lines\n3. Light Up Rows\n4. Light Each Pixel\n5. Light Random Pixel\n6. Light Up Name\n ")

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

        #Any other option the selects is not selected.
        

