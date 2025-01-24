import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 400)
sin_x = np.sin(x)
cos_x = np.cos(x)

plt.figure(figsize=(8, 6))
plt.plot(x, sin_x, label="sin(x)", linestyle="-", color="red", marker=".")
plt.plot(x, cos_x, label="cos(x)", linestyle="--", color="green", marker="x")
plt.title("Sine and Cosine Functions")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()