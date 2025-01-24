import numpy as np
import matplotlib.pyplot as plt
categories = ['Category A', 'Category B', 'Category C']
time_periods = ['T1', 'T2', 'T3', 'T4']
data = {
    'Category A': [20, 35, 30, 35],
    'Category B': [25, 32, 34, 20],
    'Category C': [15, 30, 40, 25]
}

bottom_values = np.zeros(len(time_periods))

plt.figure(figsize=(10, 6))

for category in categories:
    values = data[category]
    plt.bar(time_periods, values, bottom=bottom_values, label=category)
    bottom_values += values

plt.title("Stacked Bar Chart Showing Contributions of Categories Over Time")
plt.xlabel("Time Periods")
plt.ylabel("Values")
plt.legend(title="Categories")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()