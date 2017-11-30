import numpy as np

input_data = '''4340628 789859
-8676217 -9343493
-6306885 2927541
879935 -8934444
-8915457 4565366
-5837410 -5102154
4728191 7692896
645336 4555688
5263306 4309507
-180703 6456034
-8939483 -742053
-6934476 -7550180
-4240521 686688
6324765 -7525347
1083307 9921911
428651 -4576065
711770 1752434
-3919558 4404885
-5320025 6960376
5470440 -4235483
1525743 9633029
662363 -3746065
7325926 -8692301
-9190376 2589232'''


summa = list(map(int, input_data.split())) #making int list
# print(summa)

summa = np.array(summa) #making numpy array
#
# lenArray = len(summa)
summa.shape = (int(len(summa)/2), 3) #shaping array in two dimensional

# # print(lensumma)
#
summOfArrays = " ".join(map(str, (list(min(i) for i in summa))))
print(summOfArrays)
#