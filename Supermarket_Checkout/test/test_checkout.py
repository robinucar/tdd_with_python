from lib.Checkout import Checkout


# Add item price

def test_CanAddItemPrice():
    co = Checkout()
    co.addItemPrice("a", 1)

# Add Item
def test_CanAddItem():
    co = Checkout()
    co.addItem("a")