from decimal import Decimal

import pytest
import pandas as pd

from src.receipt import Receipt

@pytest.fixture()
def receipt2() -> Receipt:
    """Return a Receipt object to use as test data"""
    test_data = pd.DataFrame(data=[
        [0, "Apple", Decimal("0.80"), 4, Decimal("2.40")],
        [1, "Orange", Decimal("0.50"), 5, Decimal("3.00")]
    ], columns=['Item', 'Product', 'Price', 'Quantity', 'Amount']).set_index("Item")
    rec = Receipt("")
    rec.df = test_data
    return rec