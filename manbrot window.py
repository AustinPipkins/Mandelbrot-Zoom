from graphics import *
from PIL import Image as poop
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


def cor(a):
  if a < 100:
    return 0
  else:
    return (a-100)*1.63


def pos(a):
  if a > 0:
    return a
  else:
    return 0

def operate(c, numOfOp):
  z=comp(0,0)
  origin = comp(0,0)

  for i in range(numOfOp):
    prior = z
    z = z.squ() + c
    if (z.dist(origin) > 2):#also how much?
      return i
      
  return -1


#initial cords
x1,y1= -2, 1
x2,y2= 1, -1
MAINREZ = 100

SCREENX= abs(x2-x1)*MAINREZ
SCREENY= abs(y2-y1)*MAINREZ
PADDING = 60

ZOOM = .5

def drawIt(x1,y1,x2,y2):
  rez = SCREENX / abs(x2-x1)
  w,h = abs(x2-x1)*rez, abs(y2-y1)*rez

  numOfOp = int(10.0/(y1-y2)+25)
  print(numOfOp)

  disp = poop.new('RGB', (int(w),int(h)), 'white')

  screen = []
  a = 13
  b = 96
  for i in range(int(h)):
    e = y1+((y2-y1)/h)*i
    for j in range(int(w)):
      r = x1+((x2-x1)/w)*j
      point = comp(r,e)
      num = operate(point, numOfOp)
      if (num != -1):
        red = cor(abs(255 * math.cos(num/a)))
        green = cor(abs(255*math.cos((num-b)/a)))
        blue = cor(abs(255*math.cos((num-b-b)/(a))))
      else:
        red, green, blue = 0,0,0

      disp.putpixel((j,i),(int(red), int(green), int(blue)))

    if (i%math.ceil(h/10)==0):
      print(str(i/h * 100) + "%")

  disp.save("a.png")
  print("peee")
  img = Image(Point(PADDING+SCREENX/2.0+1,PADDING+SCREENY/2.0+1), "a.png")
  img.draw(win)
  print("poop")






win = GraphWin("manbro", SCREENX+PADDING*2, SCREENY+PADDING*2)
win.setBackground(color_rgb(100,100,100))
a = Rectangle(Point(PADDING,PADDING), Point(PADDING+SCREENX, PADDING+SCREENY))
a.draw(win)






drawIt(x1,y1,x2,y2)
while(True):
  click = win.getMouse()
  xc = click.getX()
  yc = click.getY()
  a = Rectangle(Point(xc-.5*ZOOM*SCREENX,yc-.5*ZOOM*SCREENY), Point(xc+.5*ZOOM*SCREENX,yc+.5*ZOOM*SCREENY))

  a.draw(win)
  click = win.getMouse()
  xc2 = click.getX()
  yc2 = click.getY()
  if (xc2 > xc-.5*ZOOM*SCREENX and xc2 < xc+.5*ZOOM*SCREENX and yc2 < yc+.5*ZOOM*SCREENY and yc2 > yc-.5*ZOOM*SCREENY):
    a.undraw()
    xc1, yc1 = xc-.5*ZOOM*SCREENX-PADDING,yc-.5*ZOOM*SCREENY-PADDING
    xc2, yc2 = xc+.5*ZOOM*SCREENX-PADDING,yc+.5*ZOOM*SCREENY-PADDING
    
    print(xc1, yc1, xc2, yc2)
    print(((xc1*(x2-x1))+(SCREENX*x1))/(SCREENX),(-(yc1*(y1-y2))+(SCREENY*y1))/(SCREENY),((xc2*(x2-x1))+(SCREENX*x1))/(SCREENX),(-(yc2*(y1-y2))+(SCREENY*y1))/(SCREENY))
    x1,y1,x2,y2 = ((xc1*(x2-x1))+(SCREENX*x1))/(SCREENX),(-(yc1*(y1-y2))+(SCREENY*y1))/(SCREENY),((xc2*(x2-x1))+(SCREENX*x1))/(SCREENX),(-(yc2*(y1-y2))+(SCREENY*y1))/(SCREENY)
    drawIt(x1,y1,x2,y2)
    
    #poo


  else:
    a.undraw()
  
  







"""



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



#==========================================================================
numOfOp = 20000
rez = 40000


x1,y1 = -1.79,.035#bottom right cord
x2,y2 = -1.74,-.035#top left cord



x,y =  0.267235642726,  -0.003347589624
r = 1.15*10**-10


x1,y1= x-r , y+r

x2,y2= x+r , y-r


#==========================================================================

def cor(a):
  if a < 100:
    return 0
  else:
    return (a-100)*2.5



prior = 0
def operate(c):
  z=comp(0,0)
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


"""
    


    
        
