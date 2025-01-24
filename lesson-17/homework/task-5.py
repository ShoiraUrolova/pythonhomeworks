import numpy as np
import matplotlib.pyplot as plt
data = np.random.normal(0, 1, 1000)

plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, alpha=0.7, color="skyblue", edgecolor="black")
plt.title("Histogram of Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()