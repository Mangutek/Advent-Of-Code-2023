import sys



import re
import math
import copy
import numpy as np
from itertools import combinations, permutations, product
import time
from matplotlib.path import Path

sys.setrecursionlimit(1000000)
file = open("C:\\Users\\Admin\\Desktop\\CodingAdvent\\dane10.txt")
mapa = []
tekst = file.readlines()
xs = 0
ys = 0
iles = 0
steps = 0
dirc = "T"

for i in range(141):
    mapa.append([])
for index ,el in enumerate(tekst):
    for element in el:
        mapa[index].append(element)
  
for indexy, el in enumerate(mapa):
    for indexx, element in enumerate(el):
        if element == "S":
            xs = indexx
            ys = indexy
start = (xs, ys)
wielekat = [start]          
def szukaj_kolejnego(x,y, iles, steps, dirc):
    symbol = mapa[y][x]
    pozycja = (x,y)
    
    if symbol == "S":
        y = y-1
        iles = iles + 1
        steps = steps+1
        
        if iles == 2:
            return symbol
        wielekat.append(pozycja)
        szukaj_kolejnego(x,y, iles, steps, dirc)
    elif symbol == "L":
        if dirc == "Left":
            dirc = "Top"
            y = y-1
            steps = steps+1
            wielekat.append(pozycja)
            szukaj_kolejnego(x,y, iles, steps, dirc)
        else:
            dirc = "R"
            x=x+1
            steps = steps+1
            wielekat.append(pozycja)
            szukaj_kolejnego(x,y, iles, steps, dirc)
    elif symbol == "J":
        if dirc == "R":
            dirc = "Top"
            y = y-1
            steps = steps+1
            wielekat.append(pozycja)
            szukaj_kolejnego(x,y, iles, steps, dirc)
        else:
            dirc = "Left"
            x=x-1
            steps = steps+1
            wielekat.append(pozycja)
            szukaj_kolejnego(x,y, iles, steps, dirc)
    elif symbol == "7":
        if dirc == "R":
            dirc = "B"
            y = y+1
            steps = steps+1
            wielekat.append(pozycja)
            szukaj_kolejnego(x,y, iles, steps, dirc)
        else:
            dirc = "Left"
            x=x-1
            steps = steps+1
            wielekat.append(pozycja)
            szukaj_kolejnego(x,y, iles, steps, dirc)
    elif symbol == "F":
        if dirc == "Left":
            dirc = "B"
            y = y+1
            steps = steps+1
            wielekat.append(pozycja)
            szukaj_kolejnego(x,y, iles, steps, dirc)
        else:
            dirc = "R"
            x=x+1
            steps = steps+1
            wielekat.append(pozycja)
            szukaj_kolejnego(x,y, iles, steps, dirc)
    elif symbol == "|":
        if dirc == "Top":
            dirc = "Top"
            y = y-1
            steps = steps+1
            wielekat.append(pozycja)
            szukaj_kolejnego(x,y, iles, steps, dirc)
        else:
            dirc = "B"
            y = y+1
            steps = steps+1
            wielekat.append(pozycja)
            szukaj_kolejnego(x,y, iles, steps, dirc)
    elif symbol == "-":
        if dirc == "R":
            dirc = "R"
            x = x+1
            steps = steps+1
            wielekat.append(pozycja)
            szukaj_kolejnego(x,y, iles, steps, dirc)
        else:
            dirc = "Left"
            x = x-1
            steps = steps+1
            wielekat.append(pozycja)
            szukaj_kolejnego(x,y, iles, steps, dirc)

szukaj_kolejnego(xs,ys, iles, steps, dirc)    
answer = 0

print(wielekat)
p = Path(wielekat)

for y in range(len(mapa)):
    for x in range(len(mapa[0])):
        if (x, y) in wielekat:
            continue
        if p.contains_point((x, y)):
            answer = answer + 1
            




print(answer)
        

