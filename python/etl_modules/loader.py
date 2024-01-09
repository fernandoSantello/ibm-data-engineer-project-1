import pandas as pd
import sqlite3 as db
from sqlalchemy import Engine

def export_csv(df: pd.DataFrame, path: str) -> None:
    df.to_csv(path_or_buf=path)

def export_sqlite3(table_name: str, df: pd.DataFrame, con: db.Connection) -> None:
    df.to_sql(name=table_name, con=con, if_exists='replace', index=False)

def execute_statment(engine: Engine, statment: str) -> pd.DataFrame:
    query_output = pd.read_sql(statment, engine)
    print(query_output)
    return query_output
