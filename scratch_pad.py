import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('BSE_data.csv')
data.plot(x='time', y='value')
plt.show()