import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "data" / "processed" / "life_tables.db"


def get_life_expectancy(sex, age):
    with sqlite3.connect(DB_PATH) as conn:
        return pd.read_sql(
            "SELECT time_period, ex FROM life_tables WHERE sex = ? AND age = ? ORDER BY time_period",
            conn,
            params=(sex, age),
        )
