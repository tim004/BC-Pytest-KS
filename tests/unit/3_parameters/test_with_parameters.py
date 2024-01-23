from pathlib import Path

import pytest

from src.receipt import Receipt

def test_verify_multiple_receipts():
    """This 1_basic tests loads a csv twice to test two cases"""
    rec1 = Receipt(Path(__file__).parents[2] / "data/unit/receipt1.csv")
    rec1.load_csv()
    rec2 = Receipt(Path(__file__).parents[2] / "data/unit/receipt2.csv")
    rec2.load_csv()
    assert rec1.verify() is True
    assert rec2.verify() is False


@pytest.mark.parametrize(
    ('input_file', 'expected_result'),
    (
        ("tests/data/unit/receipt1.csv", True),
        ("tests/data/unit/receipt2.csv", False)
    )
)
def test_verify_parametrized(input_file, expected_result, base_folder):
    """This test loads two csv files to check if the verify method returns the expected output"""
    rec = Receipt(base_folder / input_file)
    rec.load_csv()
    assert rec.verify() == expected_result


@pytest.mark.parametrize(
    ('input_data', 'expected_result'),
    (
        ("receipt1", True),
        ("receipt2", False)
    )
)
def test_verify_parametrized(input_data, expected_result, base_folder, request):
    """Use the built-in fixture called 'request' to retrieve our data from fixtures"""
    receipt = request.getfixturevalue(input_data)
    assert receipt.verify() == expected_result
