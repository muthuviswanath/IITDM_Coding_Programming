import pandas as pd
import matplotlib.pyplot as plt

ICT = {10:"Tendulkar", 18:"Virat", 45:"Rohit Sharma",7:"Dhoni"}
ser = pd.Series(ICT)
print(ser)

plt.plot(ser)
plt.show()

