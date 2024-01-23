import sys
from pathlib import Path
from decimal import Decimal

import pytest
import pandas as pd

from src.receipt import Receipt

@pytest.fixture(autouse=True)
def base_folder() -> Path:
    """Sets up a temporary directory and sets it in all path environment variables."""
    path = Path(__file__).parents[2]
    return path

@pytest.fixture(autouse=True)
def prepared_temp_folder(monkeypatch, tmp_path) -> Path:
    """Sets up a temporary directory and sets it in all path environment variables."""
    if sys.platform == "win32":
        tmp_path = Path(f"\\\\?\\{tmp_path.resolve()}")
    return tmp_path


@pytest.fixture(autouse=True)
def receipt1() -> Receipt:
    """Return a Receipt object to use as test data"""
    test_data = pd.DataFrame(data=[
        [0, "Apple", Decimal("0.80"), 3, Decimal("2.40")],
        [1, "Orange", Decimal("0.50"), 6, Decimal("3.00")]
    ], columns=['Item', 'Product', 'Price', 'Quantity', 'Amount']).set_index("Item")
    rec = Receipt("")
    rec.df = test_data
    return rec


@pytest.fixture(autouse=True)
def receipt2() -> Receipt:
    """Return a Receipt object to use as test data"""
    test_data = pd.DataFrame(data=[
        [0, "Apple", Decimal("0.80"), 4, Decimal("2.40")],
        [1, "Orange", Decimal("0.50"), 5, Decimal("3.00")]
    ], columns=['Item', 'Product', 'Price', 'Quantity', 'Amount']).set_index("Item")
    rec = Receipt("")
    rec.df = test_data
    return rec
