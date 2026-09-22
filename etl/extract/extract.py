
from pathlib import Path
import openpyxl
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "nltuk198020223.xlsx"


def extract_male_data(sheet_name):
    """ extracts the male data from the excel file
     and adds columns "male" and "time_period" for
     ease of merging data later on """
    males = pd.read_excel(
        RAW_DATA_PATH,
        sheet_name=sheet_name,
        header=5,
        usecols="A:F"  # just the males block
    )
    males["sex"] = "male"
    males["time_period"] = sheet_name
    return males


def extract_female_data(sheet_name):
    """ extracts the female data from the excel file
     and adds columns "male" and "time_period" for
     ease of merging data later on """
    females = pd.read_excel(
        RAW_DATA_PATH,
        sheet_name=sheet_name,
        header=5,
        usecols="H:M"  # just the males block
    )
    females.columns = ["age", "mx", "qx", "lx", "dx", "ex"]  
    # rename away from the .1 suffixes
    females["sex"] = "female"
    females["time_period"] = sheet_name
    return females


def extract_all_sheets():
    wb = openpyxl.load_workbook(RAW_DATA_PATH, data_only=True)
    skip_sheets = {"Contents", "Notes", "Notation", "Methodology"}
    data_sheets = [s for s in wb.sheetnames if s not in skip_sheets]

    all_data = []
    for sheet_name in data_sheets:
        all_data.append(extract_male_data(sheet_name))
        all_data.append(extract_female_data(sheet_name))

    return all_data


def combine_extracted_data(all_data):
    return pd.concat(all_data, ignore_index=True)


"""
print(combined.shape)
print(combined["time_period"].nunique())
print(combined["sex"].value_counts())
"""

all_data = extract_all_sheets()
combined = combine_extracted_data(all_data)


"""print(combined.head(10))
print(combined.tail(10))
print(combined.sample(10))
print(combined.isnull().sum())
print(combined.describe())
print(combined[
    (combined["time_period"] =="2022-2024")
    & (combined["sex"] == "male")].head())"""


"""print(combined[combined["age"] == 100][["age", "lx", "ex", "sex", "time_period"]].head())"""
