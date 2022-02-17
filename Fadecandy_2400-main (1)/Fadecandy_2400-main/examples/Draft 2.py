import opc
import time
import colorsys
import re
import random

led_colour=[(0,0,0)]*360

s = 1.0
v = 1.0

client = opc.Client('localhost:7890')

client.put_pixels(led_color)

def rainbow(pixels, order):
    if
