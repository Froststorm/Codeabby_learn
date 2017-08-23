#!
from time import sleep
from datetime import datetime
# names = ['Vita', 'Wenona', 'Judy', 'Linn', 'Douglas']

with open("text.txt", "w") as f:
    for i in range(10):
        f.write("Hello world {0} - is time \n".format(str(datetime.now())[:20]))
        sleep(1)
        print(i)

