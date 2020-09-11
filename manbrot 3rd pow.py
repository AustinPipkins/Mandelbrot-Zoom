#!/usr/bin/env python3.7
from PIL import Image
from math import sqrt
import math

class comp:
  def __init__(self, r, c):
    self.r = r
    self.c = c

  def __add__(self, other):
    new = comp(0,0)
    new.r = self.r + other.r
    new.c = self.c + other.c
    return new


  def squ(self):
    new = comp(0,0)
    new.r = self.r * self.r + self.c * self.c * -1
    new.c = self.r * self.c * 2
    return new

  def __str__(self):
    stri = "(" + str(self.r) + " + " + str(self.c) + "i)"
    return stri

  def dist(self, other):
    new = sqrt((self.r-other.r)**2+(self.c-other.c)**2)
    return new


def pos(a):
  if a > 0:
    return a
  else:
    return 0


""" mini mandolbrot
x1,y1 = -1.7595,.0195#bottom right cord
x2,y2 = -1.758,.0185#top left cord
"""

"""mini mandolbrot neck
rez = 20 * 1000 * 1000


x1,y1 = -1.7589,.0191#bottom right cord
x2,y2 = -1.75886,.01907#top left cord
"""
"""small ripple
x,y = -1.25066, 0.02012
r = 1.7 * 10**-4
"""

"""spiral
numOfOp = 30000
rez = 1000* 1000 * 1000 * 1000 * 1000
x,y = 0.2549870375144766, -0.0005679790528465
r = 1 * 10**-13
"""
""" toilet
x,y =  -0.748, 0.1
r = 0.0014
"""
#==========================================================================
numOfOp = 100
rez = 64000

x1,y1 = .365,.73#bottom right cord
x2,y2 = .375,.69#top left cord

"""

x,y =  0.267235642726,  -0.003347589624
r = 1.15*10**-10


x1,y1= x-r , y+r

x2,y2= x+r , y-r
"""

#==========================================================================

def cor(a):
  if a < 100:
    return 0
  else:
    return (a-100)*2.5



prior = 0
def operate(c):
  z=comp(0,-1.2)
  origin = comp(0,0)

  for i in range(numOfOp):
    prior = z
    z = z.squ() + c
    if (z.dist(origin) > 2):#also how much?
      return i
      
  return -1


w,h = abs(x2-x1)*rez, abs(y2-y1)*rez
print(w,h)

output = Image.new('RGB', (int(w),int(h)), 'white')

"""
i,j pixel on screen

e,r coordinate on graph

"""
#a = 60
#b = 135
a = 13
b = 96
for i in range(int(h)):
  e = y1+((y2-y1)/h)*i
  for j in range(int(w)):
    r = x1+((x2-x1)/w)*j
    point = comp(r,e)
    num = operate(point)
    if (num != -1):
      red = cor(abs(255 * math.cos(num/a)))
      green = cor(abs(255*math.cos((num-b)/a)))
      blue = cor(abs(255*math.cos((num-b-b)/(a))))
    else:
      red, green, blue = 0,0,0
    #print(red, num)
    output.putpixel((j,i),(int(red), int(green), int(blue)))

  if (i%math.ceil(h/100)==0):
    output.save("output.bmp")
    print(i/h)


output.show()
output.save("output.bmp")

    


    
        
