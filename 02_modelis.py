import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('tirs.csv')

kolonnas = [
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g"
]

X= df[kolonnas] 
y = df["species"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

modelis = DecisionTreeClassifier(max_depth=4, random_state=42)
modelis.fit(X_train, y_train)

prognozes = modelis.predict(X_test)
precizitate = accuracy_score(y_test, prognozes)

bazes_modelis = DummyClassifier(strategy="most_frequent")
bazes_modelis.fit(X_train, y_train)
bazes_prognozes = bazes_modelis.predict(X_test)
bazes_precizitate = accuracy_score(y_test, bazes_prognozes)

print(f"Modeļa precizitāte: {precizitate:.2%}")
print(f"Bāzes līnija: {bazes_precizitate:.2%}")

svarigums = pd.Series(
    modelis.feature_importances_, index=kolonnas
).sort_values(ascending=False)

print("\nDivas svarīgākās kolonnas:")
print(svarigums.head(2))

kludas = X_test[y_test != prognozes]

if not kludas.empty:
    indekss = kludas.index[0]
    pozicija = list(X_test.index).index(indekss)

    print("\nKļūdainas prognozes piemērs:")
    print(X_test.loc[indekss].to_string())
    print("Pareizā suga:", y_test.loc[indekss])
    print("Prognozētā suga:", prognozes[pozicija])
else:
    print("\nTesta datos kļūdainu prognožu nav.")