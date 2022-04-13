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
