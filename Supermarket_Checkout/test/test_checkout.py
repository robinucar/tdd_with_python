import pytest
from lib.Checkout import Checkout


@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout


# Calculate total

def test_CanCalculateTotal(checkout):
    # Add Item Price
    checkout.addItemPrice("a", 1)

    # Add Item
    checkout.addItem("a")

    # Calculate price
    assert checkout.calculateTotal() == 1

# Get Correct Total Amount With Multiple Items
def test_GetCorrectTotalWithMultipleItems(checkout):
        checkout.addItemPrice('a', 1)
        checkout.addItemPrice('b', 2)
        checkout.addItemPrice('c', 3)
        checkout.addItem('a')
        checkout.addItem('b')
        checkout.addItem('c')
        assert checkout.calculateTotal() == 6

# Add discount
def test_CanAddDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)
