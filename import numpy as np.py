import numpy as np
import matplotlib.pyplot as plt
f = open(r"C:\Computational Methods in Physics\jellyhunt.txt", "r")
time_ = []
jellyfishes = []
for line in f:
  currentLine = line.split(",")
  time_.append(float(currentLine[0]))
  jellyfishes.append(float(currentLine[1]))
curveFit = np.poly1d(np.polyfit(time_, jellyfishes, 3))
print(curveFit)
plt.scatter(time_, jellyfishes)
plt.plot(time_, curveFit(time_), '--', color='red')
plt.show()