import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data
data = pd.read_csv("chart_1_chiber.csv")

# Create a simple line chart
print(data['time'])
plt.plot(data['time'], data['elevation'])
plt.title('Sample Chart')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
