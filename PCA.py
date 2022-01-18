import pandas as pandas
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

city  = "Comune"
population = "Popolazione"
income = "Reddito"
business = "Imprese attive"
waste = "Rifiuti urbani"
waste_sorted = "Raccolta differenziata"
waste_ratio = "Rapporto differenziata/non differenziata"
mean = "Sopra/Sotto la media"

target = waste

dataFrame = pandas.read_csv('data.csv')
features = [population, income, business]

meanTarget = dataFrame[target].mean()

dataFrame[mean] = dataFrame.apply(lambda row: ('Sotto' if row[target] < meanTarget else 'Sopra'), axis=1)

featuresDF = dataFrame.loc[:, features]
targetDF = dataFrame.loc[:, mean]

# Standardizzo i dati
featuresDF = StandardScaler().fit_transform(featuresDF)

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(featuresDF)

variance_ratio = pca.explained_variance_ratio_
principalDF = pandas.DataFrame(data = principalComponents, columns=['Principal component 1', 'Principal component 2'])
finalDf = pandas.concat([principalDF, targetDF], axis = 1)

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel(f'PC 1 ({round(variance_ratio[0]*100), 1}%)', fontsize = 15)
ax.set_ylabel(f'PC 2 ({round(variance_ratio[1]*100, 1)}%)', fontsize = 15)

title = f"Media di {target.lower()}\nComponenti iniziali:"
for component in features:
    title = title + f" {component.lower()}"
ax.set_title(title, fontsize = 20)

targets = ['Sopra', 'Sotto']
colors = ['r', 'g']
for target_graph, color in zip(targets,colors):
    indicesToKeep = finalDf[mean] == target_graph
    ax.scatter(finalDf.loc[indicesToKeep, 'Principal component 1']
               , finalDf.loc[indicesToKeep, 'Principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()
plt.savefig(f"PCA {target.lower()}.png")