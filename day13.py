import numpy

file = open("C:\\Users\\Admin\\Desktop\\CodingAdvent\\dane13.txt")
tekst = file.read().strip().split("\n\n")
mapy = []
for matrix in tekst:
    mapy.append(matrix.split())

def printmatrix(matrix):
    print(len(matrix), len(matrix[0]))
    string = ""
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            string = string + str(matrix[y][x]) + " "
        print(string)
        string = ""

def szukaj(matryca):
    for x in range(1, len(matryca)):
        y = x if x < len(matryca) - x else len(matryca) - x
        cz_1 = matryca[:x][::-1][:y]
        cz_2 = matryca[x:][:y]
        if numpy.sum(cz_1 ^ cz_2) == 1: #part1 ==0, part2==1
            return x

razem = 0
for mapa in mapy:
    mapa_logic = numpy.array([[symbol == "#" for symbol in linia] for linia in mapa])
    wynik = szukaj(mapa_logic)
    wynik_t = szukaj(mapa_logic.T)
    razem += wynik * 100 if wynik else wynik_t

print(razem)
