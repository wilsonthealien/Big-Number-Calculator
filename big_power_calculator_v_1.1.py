from math import *
from kandinsky import *
from ion import *
from random import *
from time import *
from kandinsky import draw_string as locate
from kandinsky import fill_rect as fill
from ion import keydown as key

x=15
R=randint(0,100)
G=randint(0,100)
B=randint(0,100)
bg_1=(R,G,B)
bg_2=(78,13,47)
num=input("Number? ")
power=input("Power? ")

calc=int(num)**int(power)
digits=len(str(calc))
int_string=str(calc)
calc_length=len(int_string)

mypixels=[(0,90,322,2,"white"),
(0,125,322,2,"white")
]
fill(0,0,322,222,bg_2)
for r in mypixels:
    fill(*r)
while True:
  
  locate("Left/Right arrow = left & right",0,0,"white",bg_2)  
  locate(num+"^"+power+" = "+ str(calc),x,100,"white",bg_2)
  locate("RGB= "+str(R)+","+str(G)+","+str(B),160,200)
  
  if key(KEY_LEFT):
    for i in range(1):
      x-=1
  if key(KEY_RIGHT):
    for i in range(1):
      x+=1
  if x>22:
    x=22
