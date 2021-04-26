# importing the required module 
import matplotlib.pyplot as plt 
from stringToArray import * 
import sys


# x axis values 
x = StringToFloatArray(sys.argv[1])
# corresponding y axis values 
y = StringToFloatArray(sys.argv[2])

# plotting the points 
plt.plot(x, y) 

# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 

# giving a title to my graph 
plt.title('My first graph!') 

# function to show the plot or save it to a file
plt.show() 

print("[DONE]")



