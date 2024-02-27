import pandas as pa
import matplotlib.pyplot as plt
indian_population_2011 = {'Assam':234563,'Telangana':345678,'Karnataka':4567890,'MadhyaPradesh':3456784}
indian_population_2021 = {'Assam':234733,'Telangana':348345,'Karnataka':6789043,'MadhyaPradesh':5678934}
s_2011 = pa.Series(indian_population_2011)
s_2021 = pa.Series(indian_population_2021)
population_growth = s_2021-s_2011

x = population_growth.index
y = population_growth.values
plt.figure(figsize=(15,6))
plt.xticks(rotation='horizontal',size=10)
plt.bar(x,y, color='purple')
plt.show()

