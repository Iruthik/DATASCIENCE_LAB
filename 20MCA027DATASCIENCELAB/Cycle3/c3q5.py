import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Walking","Cycling ","Car","Bus","Train"])
y = np.array([25, 15, 35, 18,3])
plt.title("Students Transportation Graph")
plt.xlabel("Mode of Transport")
plt.ylabel("Frequency")
plt.bar(x,y,color='g',width=.1)
plt.show()