import pandas as pd
import numpy as np

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(columns=[('UN region', 'UN region'),
       ('IMF[1][13]', 'Year'), ('World Bank[14]', 'Estimate'),
       ('World Bank[14]', 'Year'), ('United Nations[15]', 'Estimate'),
       ('United Nations[15]', 'Year')])
    df.columns = [col for col in df.columns.values]
    columns = df.columns.tolist()
    columns[0] = 'Country'
    columns[1] = 'GDP_USD_millions'
    df.columns = columns
    df = df[(df['GDP_USD_millions'] != '—') & (df['Country'] != 'World')]
    df = df.reset_index(drop=True)
    df['GDP_USD_millions'] = df['GDP_USD_millions'].astype(float)
    df['GDP_USD_millions'] = np.round(df['GDP_USD_millions'] / 1000,2)
    df = df.rename(columns = {"GDP_USD_millions":"GDP_USD_billions"})
    return df
