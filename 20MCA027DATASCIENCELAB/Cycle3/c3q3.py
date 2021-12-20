import matplotlib
import matplotlib.pyplot as plt
import numpy as np


x = np.array(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
y = np.array([173,153,195,147,120,144,148,109,174,130,172,131])

plt.title("Sales Data")
plt.xlabel('Months of Year', fontsize=18)
plt.ylabel("Sales of Segments")
plt.scatter(x, y,color='pink')


x = np.array(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
y = np.array([189,189,105,112,173,109,151,197,174,145,177,161])
plt.scatter(x, y,color='y')



x = np.array(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
y = np.array([185,185,126,134,196,153,112,133,200,145,167,110])
plt.scatter(x, y,color='blue')
plt.show()

