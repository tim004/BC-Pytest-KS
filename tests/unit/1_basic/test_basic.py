from pathlib import Path
from decimal import Decimal

import pytest
import pandas as pd

from src.receipt import Receipt

def test_verify_receipt1():
    """Basic unit test where the data is loaded from the file first. Note that an error while loading will cause the test to fail"""
    receipt = Receipt(Path(__file__).parents[2] / "data/unit/receipt1.csv")
    receipt.load_csv()
    assert receipt.verify() is True


def test_verify_receipt2():
    """Basic unit test where the data is loaded from the file first. Note that an error while loading will cause the test to fail"""
    receipt = Receipt(Path(__file__).parents[2] / "data/unit/receipt2.csv")
    receipt.load_csv()
    assert receipt.verify() is False


def test_verify_receipt_with_data():
    """Basic unit test where the data is loaded without using the load_csv method first"""
    test_data = pd.DataFrame(data=[
        [0, "Apple", Decimal("0.80"), 3, Decimal("2.40")],
        [1, "Orange", Decimal("0.50"), 6, Decimal("3.00")]
    ], columns=['Item', 'Product', 'Price', 'Quantity', 'Amount']).set_index("Item")
    receipt = Receipt("")
    receipt.df = test_data
    assert receipt.verify() is True
