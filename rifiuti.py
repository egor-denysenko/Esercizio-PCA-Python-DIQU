
import pandas as pandas
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

pandas.set_option("display.max_rows", None, "display.max_columns", None)

# Dichiarazione delle colonne
code = "Codice territorio"
city  = "Comune"
population = "Popolazione"
income = "Reddito"
business = "Imprese attive"
waste = "Rifiuti urbani"
waste_sorted = "Raccolta differenziata"
waste_ratio = "Rapporto differenziata/non differenziata"


# Carico CSV della popolazione
populationDF = pandas.read_csv('Popolazione.csv')
populationDF.drop(code, axis=1, inplace=True)

# Carico CSV delle imprese
businessDF = pandas.read_csv('Imprese.csv')
businessDF.drop(code, axis=1, inplace=True)

# Carico CSV dei redditi
incomeDF = pandas.read_csv('Redditi.csv')
incomeDF.drop(code, axis=1, inplace=True)

# Carico CSV dei rifiuti
trashDF = pandas.read_csv('Rifiuti.csv')

# Unisco le 3 tabelle
dataFile = populationDF.merge(businessDF, on=city)
dataFile = dataFile.merge(incomeDF, on=city)
dataFile = dataFile.merge(trashDF, on=city)

# Calcolo il rapporto tra rifiuti normali e raccolta differenziata
dataFile[waste_ratio] = dataFile.apply(lambda row: (row[waste_sorted]/row[waste]), axis=1)

# Calcolo i valori per abitante 
dataFile[income] = dataFile.apply(lambda row: (row[income]/row[population]), axis=1)
dataFile[business] = dataFile.apply(lambda row: (row[business]/row[population]), axis=1)
dataFile[waste] = dataFile.apply(lambda row: (row[waste]/row[population]), axis=1)
dataFile[waste_sorted] = dataFile.apply(lambda row: (row[waste_sorted]/row[population]), axis=1)

print(dataFile.head())

plt.figure(figsize=(20,10))

c = dataFile.corr()

sns.heatmap(c, vmin=-1, vmax=1, cmap='coolwarm')
plt.show()