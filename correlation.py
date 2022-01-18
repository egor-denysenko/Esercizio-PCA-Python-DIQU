
import pandas as pandas
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

pandas.set_option("display.max_rows", None, "display.max_columns", None)

# Carico CSV dei dati
dataFrame = pandas.read_csv('data.csv')

print(dataFrame.head())

# Creo e stampo la mappa di correlazione

plt.figure(figsize=(20,10))
correlationMap = dataFrame.corr()
sns.heatmap(correlationMap, vmin=-1, vmax=1, cmap='coolwarm', annot=True)
plt.savefig('Heatmap correlazione.png')