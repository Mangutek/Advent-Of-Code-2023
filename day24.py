#rozwiązuje tylko part1

file = open("C:\\Users\\Admin\\Desktop\\CodingAdvent\\dane24.txt")
tekst = file.readlines()
instrukcja = []
wzory = []
miejsca = []
zmiana = []
cross = []
answer = 0

min = 200000000000000
max = 400000000000000

for line in tekst:
    roz1 = line.split("@ ")
    punkty = roz1[0].split(", ")
    velo = roz1[1].split(", ")
    instrukcja.append([punkty[0],punkty[1],velo[0],velo[1]])


for ins in instrukcja:
    pozycjaA = [int(ins[0]), int(ins[1])]
    pozycjaB = [int(ins[0])+int((ins[2])), int(ins[1])+int(ins[3])]
    
    a = (int(pozycjaB[1]) - int(pozycjaA[1]) )/(int(pozycjaB[0])-int(pozycjaA[0]))
    b = (-(int(pozycjaA[0]))*a)+int(pozycjaA[1])
    wzor = [a, b]
    wzory.append(wzor)
    zm = [pozycjaA, pozycjaB]
    zmiana.append(zm)



for i in range(0, len(wzory)):
    for n in range(i+1, len(wzory)):
        tak = 0
        if (wzory[n][0]- wzory[i][0]) != 0:
            x = (wzory[i][1] - wzory[n][1])/(wzory[n][0]- wzory[i][0])
            y = wzory[i][0] * x + wzory[i][1]
            if (zmiana[i][0][0] - zmiana[i][1][0] < 0) and (zmiana[i][0][0] - x < 0):
                tak += 1
                
            elif (zmiana[i][0][0] - zmiana[i][1][0] > 0) and (zmiana[i][0][0] - x > 0):
                tak += 1
                
            if tak > 0:
                if (zmiana[n][0][0] - zmiana[n][1][0] > 0) and (zmiana[n][0][0] - x > 0):

                    cross.append([x, y ])
                elif (zmiana[n][0][0] - zmiana[n][1][0] < 0) and (zmiana[n][0][0] - x < 0):

                    cross.append([x, y ])
                else:
                    continue
            else:
                continue
        else:
             continue



for el in cross:
    if (el[0] >= min and el[1] >= min) and (el[0] <= max and el[1] <= max):
        print(el)
        answer += 1


print(answer) 









    

