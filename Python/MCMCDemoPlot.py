import numpy as np
import matplotlib.pyplot as plt
from stringToArray import * 
import sys
import csv

csvFile = open(sys.argv[1], "r")
reader = csv.reader(csvFile)


# x axis values 
x = []
# corresponding y axis values cost 1, 2, 3
y0 = []
y1 = []
y2 = []

i = 0
for item in reader:
    if i==0:
        i = 1
        continue
    x.append(float(item[0]))
    y0.append(float(item[1]))
    y1.append(float(item[2]))
    y2.append(float(item[3]))
    

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False


plt.plot(x,y0,color='green',label='To surface')
plt.plot(x,y1,color='red',label='To each other')
plt.plot(x,y2,color='blue',label='Geometry at original')

plt.title(u'Demo Figure')
plt.ylabel(u'Cost')
plt.ylim(0, 1.2)

plt.legend()

plt.show()