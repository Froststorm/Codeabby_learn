import numpy as np

# rows = int(input("Input number of inputs "))
# cols = int(input("Input number of columns "))

# for _ in range(rows):
#     summa.append(int(input("input number{0}: ".format(_))))

# print(summa)
innn = '''387155 403288
570987 389873
919808 266742
78702 555831
447207 40009
812595 316003
40224 697880
840806 184311
131352 770345
724314 314366
172776 411959
465876 954219'''

print(innn)
# summa = innn.split()
# print(summa)

summa = list(map(int, innn.split())) #making int list
# print(summa)

summa = np.array(summa) #making numpy array
#
# lenArray = len(summa)
summa.shape = (int(len(summa)/2), 2) #shaping array in two dimensional

# # print(lensumma)
#
summOfArrays = list(map(sum, summa))
print(' '.join(map(str, summOfArrays)))
#

# Array = [[0 for row in range(2)] for col in range(int(15))]
# Array = []
#
# for i in range(15):
#     # print(i)
#     Array.append([])
#     for j in range(2):
#         Array[i].append  # (int(input("input number: ")))
#
# print(Array)
#
# for _ in Array:
#     print(sum(_), end=' ')




