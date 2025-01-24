import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 400)
f1 = x**2 - 4*x + 4

plt.figure(figsize=(8, 6))
plt.plot(x, f1, label="f(x) = x^2 - 4x + 4", color="blue")
plt.title("Plot of f(x) = x^2 - 4x + 4")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()