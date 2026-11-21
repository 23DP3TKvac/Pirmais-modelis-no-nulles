import pandas as pd 

df = pd.read_csv('dati/penguins.csv')

sakuma_skaits = len(df)

df = df.drop_duplicates()
dublikati = sakuma_skaits - len(df)

pirms = len(df)
df = df.dropna()
trukstosas = pirms - len(df)

df.to_csv('tirs.csv', index=False)

print("Rindas sākumā:", sakuma_skaits)
print("Izmestie dublikāti:", dublikati)
print("Izmestās rindas ar tukšām vērtībām:", trukstosas)
print("Rindas beigās:", len(df))