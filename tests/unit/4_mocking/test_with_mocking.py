import mock
import pytest

from src.receipt import Receipt


"""
Tests in this file makes use of the temp_folder fixture defined in 4_mocking/conftest.py
If the temp_folder is not used, the test will write the output data to the project folder itself.
"""


def test_create_updated_receipt1(base_folder, temp_folder):
    """Tests whether a new receipt is saved"""
    rec = Receipt(temp_folder / "data/unit/receipt1.csv")
    rec.create_updated_receipt()
    assert (temp_folder / "data/unit/total_receipt1.csv").exists()


#This test will fail because the verify method will prevent the total_receipt2.csv file from being created
#Using xfail marks it as an expected failure
@pytest.mark.xfail()
def test_create_updated_receipt2(base_folder, temp_folder):
    """Tests whether a new receipt is saved"""
    rec = Receipt(temp_folder / "data/unit/receipt2.csv")
    rec.create_updated_receipt()
    assert (temp_folder / "data/unit/total_receipt2.csv").exists()

#This function will always return True and can be used as a substitute for the verify method of Receipt
def verify_always_returns_true(cls, *args, **kwargs):
    return True


@mock.patch('src.receipt.Receipt.verify')
def test_create_updated_receipt2_patched(verify_always_returns_true, base_folder, temp_folder):
    """Tests whether a new receipt is saved while mocking the verify method using @patch"""
    rec = Receipt(temp_folder / "data/unit/receipt2.csv")
    rec.create_updated_receipt()
    assert (temp_folder / "data/unit/total_receipt2.csv").exists()


def test_create_updated_receipt2_using_patched_alternative(base_folder, temp_folder):
    """Tests whether a new receipt is saved while mocking the verify method using with mock.patch.object"""
    with mock.patch.object(Receipt, 'verify', new=verify_always_returns_true):
        rec = Receipt(temp_folder / "data/unit/receipt2.csv")
        rec.create_updated_receipt()
        assert (temp_folder / "data/unit/total_receipt2.csv").exists()

