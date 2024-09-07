import os
import pandas as pd
import csv


WEY_TO_FILE_CSV = os.path.join(os.path.dirname(__file__), "../csv_excel/transactions.csv")

WEY_TO_FILE_EXCEL = os.path.join(os.path.dirname(__file__), "../csv_excel/transactions_excel.xlsx")

def reading_financial_transactions_csv(WEY_TO_FILE_CSV: str) -> list[str]:
    with open(WEY_TO_FILE_CSV, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=';')
        new_list = []
        for row in reader:
            new_list.append(row)
        return new_list


def reading_financial_transactions_excel(WEY_TO_FILE_EXCEL: str) -> list[dict]:
    df = pd.read_excel(WEY_TO_FILE_EXCEL)
    return df.to_dict(orient="records")


print(reading_financial_transactions_csv(WEY_TO_FILE_CSV))
