import pandas as pd


def fill_missing_values(df, column, value):
    """Rellena valores faltantes en una columna específica."""
    df.loc[:, column] = df[column].fillna(value)  # Usa .loc para asignar
    return df

def remove_duplicates(df):
    """Elimina filas duplicadas del DataFrame."""
    return df.drop_duplicates()

def normalize_text(df, column):
    """Convierte texto en una columna a formato título."""
    df.loc[:, column] = df[column].str.title()  # Usa .loc para asignar
    return df
