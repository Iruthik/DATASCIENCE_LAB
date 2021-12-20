

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array(["Mon","Tue","Wed","Thu","Fri"])
y = np.array([300,450,150,400,650])


plt.subplot(2, 1, 1)
plt.xlabel("Days of Week")
plt.ylabel("Sales of Drinks")
plt.title("Sales data1",loc="right")
plt.plot(x,y,marker='H',mfc='m',mec='k',ls=':',color='c')
plt.grid(color='b',linestyle='-.')

#plot 2:
    
x = np.array(["Mon","Tue","Wed","Thu","Fri"])
y = np.array([400, 500, 350, 300,500])

plt.subplot(2, 1, 2)
plt.xlabel("Days of Week")
plt.ylabel("Sales of Food")
plt.title("Sales data2",loc="center")
plt.plot(x,y,marker='d',mfc='g',mec='r',ls='-.',color='y')
plt.grid(color='b',linestyle='-.')
plt.show()