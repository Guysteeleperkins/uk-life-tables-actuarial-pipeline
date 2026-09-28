
import pandas as pd


def split_time_period(combined):
    combined = combined.copy() 
    combined["start_year"] = combined["time_period"].str.split("-").str[0].astype(int)
    combined["end_year"] = combined["time_period"].str.split("-").str[1].astype(int)
    return combined


def cast_dyptes(combined):
    combined = combined.copy()
    combined["age"] = combined["age"].astype(int)
    combined[["mx", "qx", "lx", "dx", "ex"]] = combined[
        ["mx", "qx", "lx", "dx", "ex"]
    ].astype(float)
    return combined


def validate(df):
    assert len(df) == 43 * 2 * 101, f"unexpected row count: {len(df)}"
    assert not df.duplicated(["time_period", "sex", "age"]).any(), "duplicate rows found"
    assert df["qx"].between(0, 1).all(), "qx outside the range 0 to 1"
    assert df.isnull().sum().sum() == 0, "null values found"
    return df
