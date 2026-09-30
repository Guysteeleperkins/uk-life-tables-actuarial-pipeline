import sqlite3
from contextlib import closing
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
EXCEL_PATH = PROCESSED_DIR / "CleanedNationalLifeTables.xlsx"
DB_PATH = PROJECT_ROOT / "data" / "processed" / "life_tables.db"
SCHEMA_PATH = PROJECT_ROOT / "etl" / "sql" / "schema.sql"


def export_to_excel(df):
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_excel(EXCEL_PATH, index=False)
    return EXCEL_PATH


def load_to_sqlite(df):
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.executescript(SCHEMA_PATH.read_text())
        df.to_sql("life_tables", conn, if_exists="append", index=False)
        conn.commit()
        count = conn.execute("SELECT COUNT(*) FROM life_tables").fetchone()[0]
    assert count == len(df), f"Loaded {count} rows, expected{len(df)}"
    return count

