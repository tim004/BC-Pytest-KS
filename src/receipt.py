from pathlib import Path
from decimal import Decimal

import pandas as pd


def decimal_from_value(value):
    return Decimal(value)

class Receipt:
    path = None
    df = None
    def __init__(self,path):
        self.path = Path(path)

    def load_csv(self):
        self.df = pd.read_csv(self.path, index_col="Item",
                              converters={'Price': decimal_from_value, 'Amount': decimal_from_value})

    def verify(self):
        for index, row in self.df.iterrows():
            if row["Price"] * row["Quantity"] != row["Amount"]:
                return False
        return True

    def add_total(self):
        total_row = [None, None, None, sum(self.df["Amount"])]
        self.df.loc["Total"] = total_row

    def save(self):
        total_file_name = "total_" + self.path.name
        total_file_path = self.path.parent / total_file_name
        self.df.to_csv(total_file_path)

    def create_updated_receipt(self):
        self.load_csv()
        if self.verify():
            self.add_total()
            self.save()


if __name__ == '__main__':
    receipt = Receipt(Path(__file__).parents[1] / "tests/data/unit/receipt1.csv")
    receipt.load_csv()
    print(receipt.df)
    receipt.add_total()
    print(receipt.df)