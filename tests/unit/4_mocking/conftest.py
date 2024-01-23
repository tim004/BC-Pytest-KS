import sys
from pathlib import Path
from decimal import Decimal
import shutil

import pytest
import pandas as pd

from src.receipt import Receipt

@pytest.fixture(autouse=True)
def base_folder() -> Path:
    """Defines a base folder where other file paths can be derived from"""
    path = Path(__file__).parents[2]
    return path


@pytest.fixture(autouse=True)
def temp_folder(base_folder, tmp_path) -> Path:
    """
    Sets up a temporary directory and copies the tests/data folder to it.
    Note the use of the built-in tmp_path fixture
    """
    if sys.platform == "win32":
        tmp_path = Path(f"\\\\?\\{tmp_path.resolve()}")
    shutil.copytree(base_folder / "data", Path(tmp_path) / "data")
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
