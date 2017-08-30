listOfNums = '''
9401421 985
8505541 773
-9426701 -2866199
7231017 -3042341
9829 1608
8232982 559
11569 476
1181042 2648374
8802196 757
18979 1650
1997014 714
3713742 548
8767994 577
5273828 438'''

def div(a, b):
    return round(a / b)

listOfNums = [int(x) for x in listOfNums.split()]

mas = []
index = 0

lenOfArray = len(listOfNums) // 2  # array length

for i in range(lenOfArray):
    mas.append([])
    for j in range(2):
        mas[i].append(listOfNums[index])
        index += 1

stringOfRounded = " ".join(str(div(x[0], x[1])) for x in mas)

print(stringOfRounded)
