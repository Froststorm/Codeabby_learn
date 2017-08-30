# import numpy as np
while True:
    try:
        dimOfArray = int(input("Array dim: "))
        break
    except:
        print("Not an integer! ")

input_data = '''-114120 6951595 -9606087
-8878887 -1213744 -7260789
-7684657 -4506397 2477313
-7694809 -3970611 -6992120
-8193674 5938701 -2862604
7442160 -4493918 -7217390
-942925 -1947933 -6526931
-4228345 7559164 181977
-1013545 5999362 -5100927
-5798193 -4652745 1447967
-4512630 5233135 -1600438
-4118718 6354248 7185818
-13795307 8669590 -7320579
-8902194 -9025218 -1291190
-5894314 -7218893 -5352489
1243081 -9776732 153593
4025691 -719658 8205659
7498760 5051997 5764823
-2319262 -5961548 1764186
2579811 -1759741 7111440'''

summa = [int(x) for x in input_data.split()] #making int list

print(summa, end="\n\n\n")

mas = []
index = 0

lenOfArray = len(summa)//dimOfArray # array length

for i in range(lenOfArray):
    mas.append([])
    for j in range(dimOfArray):
        mas[i].append(summa[index])
        index += 1  # index count
# summa.shape = (int(len(summa)/3), 3) #shaping array in two dimensional of 3 items
#
# print(mas, end="\n\n\n")


# minimumOfArray =
print([min(i) for i in mas])

# summOfArrays = " ".join([str(x) for x in ])
# print(summOfArrays)
