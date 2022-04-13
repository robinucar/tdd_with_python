import pytest
from lib.Checkout import Checkout


@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice('a', 1)
    checkout.addItemPrice('b', 2)
    checkout.addItemPrice('c', 3)
    return checkout


# Calculate total

def test_CanCalculateTotal(checkout):
    # Add Item
    checkout.addItem("a")

    # Calculate price
    assert checkout.calculateTotal() == 1

# Get Correct Total Amount With Multiple Items


def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItem('a')
    checkout.addItem('b')
    checkout.addItem('c')
    assert checkout.calculateTotal() == 6

# Add discount


def test_CanAddDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2) 

# Apply Discount to the total
def test_canApplyDiscountRule(checkout):
    checkout.addDiscount('a', 3, 2)
    checkout.addItem('a')
    checkout.addItem('a')
    checkout.addItem('a')
    assert checkout.calculateTotal() == 2

# Exception is thrown for item added without price
def test_ExceptionWithBadItem(checkout):
    with pytest.raises(Exception):
        checkout.addItem("d")