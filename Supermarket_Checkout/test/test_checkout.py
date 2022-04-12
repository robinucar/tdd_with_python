# Create instance of Checkout class
from lib.Checkout import Checkout


def test_CanInstantiateCheckout():
    co = Checkout()

# Add item price


def test_CanAddItemPrice():
    co = Checkout()
    co.addItemPrice("a", 1)
