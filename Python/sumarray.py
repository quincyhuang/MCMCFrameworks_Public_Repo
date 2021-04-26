import sys
from stringToArray import *

sum = 0
data = StringToFloatArray(sys.argv[1])

for i in range(0, len(data), 1):
    sum += data[i]


print(sum)