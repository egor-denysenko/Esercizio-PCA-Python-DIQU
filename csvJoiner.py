import pandas as pandas

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
dataFrame = populationDF.merge(businessDF, on=city)
dataFrame = dataFrame.merge(incomeDF, on=city)
dataFrame = dataFrame.merge(trashDF, on=city)

# Calcolo il rapporto tra rifiuti normali e raccolta differenziata
dataFrame[waste_ratio] = dataFrame.apply(lambda row: (row[waste_sorted]/row[waste]), axis=1)

# Calcolo i valori per abitante 
dataFrame[income] = dataFrame.apply(lambda row: (row[income]/row[population]), axis=1)
dataFrame[business] = dataFrame.apply(lambda row: (row[business]/row[population]), axis=1)
dataFrame[waste] = dataFrame.apply(lambda row: (row[waste]/row[population]), axis=1)
dataFrame[waste_sorted] = dataFrame.apply(lambda row: (row[waste_sorted]/row[population]), axis=1)

dataFrame.to_csv('data.csv', index=False)