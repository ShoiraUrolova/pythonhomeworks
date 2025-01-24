import numpy as np
import matplotlib.pyplot as plt
x_rand = np.random.uniform(0, 10, 100)
y_rand = np.random.uniform(0, 10, 100)

plt.figure(figsize=(8, 6))
plt.scatter(x_rand, y_rand, color="orange", marker="o", edgecolor="black")
plt.title("Scatter Plot of Random Points")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()