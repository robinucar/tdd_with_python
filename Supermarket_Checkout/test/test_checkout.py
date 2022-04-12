import pytest
from lib.Checkout import Checkout


@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout


# Add item price
def test_CanAddItemPrice(checkout):

    checkout.addItemPrice("a", 1)

# Add Item
def test_CanAddItem(checkout):

    checkout.addItem("a")
