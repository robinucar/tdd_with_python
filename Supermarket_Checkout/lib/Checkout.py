# create class
class Checkout:
    def __init__(self):
        self.prices = {}
        self.total = 0
    # create add item and price method
    def addItemPrice(self, item, price):
        self.prices[item] = price

    # add item
    def addItem(self, item):
        self.total += self.prices[item]

    # Calculate total
    def calculateTotal(self):
        return self.total
