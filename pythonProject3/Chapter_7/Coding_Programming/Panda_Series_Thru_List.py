import pandas as pa
import matplotlib.pyplot as plt
fest = ['Treasure Hunt', 'Wall Art', 'Code Champ', 'Singing']
s = pa.Series(fest)
print(s)

plt.plot(s)
plt.show()
