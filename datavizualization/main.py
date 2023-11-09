import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("file.xlsx", skiprows=2)
data = data.iloc[:, 1:]
data = data.set_index("Date")
data_grouped = data.groupby("Date")["Count"].sum().reset_index()
data_grouped["New_Index"] = range(1, len(data_grouped) + 1)
print(data) 




plt.plot(data_grouped["New_Index"], data_grouped['Count'])
plt.xticks(data_grouped["New_Index"], data_grouped["Date"], rotation=45)
plt.xlabel('Date')
plt.ylabel('Product Purchase Quanity')
plt.show()