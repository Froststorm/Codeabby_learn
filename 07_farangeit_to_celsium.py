def toCelsium(a):
    return round(5/9*(a-32))

listOfNums = [int(input())]

listOfNums = [int(x) for x in listOfNums.split()]
print(listOfNums[1::], end="\n\n\n")

# for i in range(34):
print(" ".join([str(toCelsium(i)) for i in listOfNums[1:]]))


