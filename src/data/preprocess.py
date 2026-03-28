import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df


def clean_data(df):
    # Eliminar columna innecesaria
    df = df.drop("customerID", axis=1)

    # Convertir TotalCharges a numérico
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Eliminar nulos
    df = df.dropna()

    # Crear variable tenure_group
    df["tenure_group"] = pd.cut(
    df["tenure"],
    bins=[0, 12, 24, 48, 60, 100],
    labels=["0-1yr", "1-2yr", "2-4yr", "4-5yr", "5+yr"]
   )

    return df


def encode_data(df):
    # Convertir target a numérico
    df["Churn"] = df["Churn"].map({"No": 0, "Yes": 1})

    # One-hot encoding
    df = pd.get_dummies(df, drop_first=True)

    return df


def preprocess(path):
    df = load_data(path)
    df = clean_data(df)
    df = encode_data(df)
    return df


if __name__ == "__main__":
    df = preprocess("data/churn.csv")
    print(df.head())
    print("Shape:", df.shape)