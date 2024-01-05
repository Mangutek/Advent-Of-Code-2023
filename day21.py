#tylko part1
from matplotlib.path import Path
import numpy

file = open("C:\\Users\\Admin\\Desktop\\CodingAdvent\\day21.txt")
tekst = file.readlines()
mapa = []
pozycje = []


def printmatrix(matrix):
    print(len(matrix), len(matrix[0]))
    string = ""
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            string = string + str(matrix[y][x]) + " "
        print(string)
        string = ""


for index ,el in enumerate(tekst):
    mapa.append([])
    for element in el:
        mapa[index].append(element)

for y in range(len(mapa)):
    for x in range(len(mapa[0])-1):
        if mapa[y][x] == "S":
            startpos = [[x, y]]
            mapa[y][x] = "."
            break

x_lex = len(mapa[0])
y_len = len(mapa)

pozycje.append(startpos)

def find_nextpos(step):
    el = pozycje[step]
    pozycje.append([])
    for element in el:
        x = element[1]
        y = element[0]
        #góra
        if mapa[y-1][x] == ".":
            if [y-1 ,x] not in pozycje[step+1]:
                pozycje[step+1].append([y-1, x])

        #dół
        if mapa[y+1][x] == ".":
            if [y+1 ,x] not in pozycje[step+1]:
                pozycje[step+1].append([y+1, x])

        #lewo
        if mapa[y][x-1] == ".":
            if [y ,x-1] not in pozycje[step+1]:
                pozycje[step+1].append([y, x-1])

        #prawo
        if mapa[y][x+1] == ".":
            if [y ,x+1] not in pozycje[step+1]:
                pozycje[step+1].append([y, x+1])       

for i in range(0, 64):
    find_nextpos(i)
    print(len(pozycje[i+1]))
