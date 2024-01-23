from decimal import Decimal


import pytest
import pandas as pd

from src.receipt import Receipt

@pytest.fixture()
def receipt1() -> Receipt:
    """Return a Receipt object to use as test data"""
    test_data = pd.DataFrame(data=[
        [0, "Apple", Decimal("0.80"), 3, Decimal("2.40")],
        [1, "Orange", Decimal("0.50"), 6, Decimal("3.00")]
    ], columns=['Item', 'Product', 'Price', 'Quantity', 'Amount']).set_index("Item")
    rec = Receipt("")
    rec.df = test_data
    return rec


def test_verify_receipt_with_fixture(receipt1):
    """This test uses the receipt1 fixture to only test the verify method"""
    assert receipt1.verify() is True

@pytest.fixture()
def output1() -> pd.DataFrame:
    """Return a Receipt object to use as test data"""
    test_output = pd.DataFrame(data=[
        [0, "Apple", Decimal("0.80"), 3, Decimal("2.40")],
        [1, "Orange", Decimal("0.50"), 6, Decimal("3.00")],
        ["Total", None, None, None, Decimal("5.40")]
    ], columns=['Item', 'Product', 'Price', 'Quantity', 'Amount'], dtype= "object").set_index("Item")
    return test_output

def test_add_total_with_fixture(receipt1, output1):
    """This test use the receipt1 fixture to only test the add_total method"""
    receipt1.add_total()
    pd.testing.assert_frame_equal(receipt1.df, output1)


def test_verify_receipt_with_fixture_from_conftest(receipt2):
    """This test use the receipt1 fixture from confest.py to only test the verify method"""
    assert receipt2.verify() is False

