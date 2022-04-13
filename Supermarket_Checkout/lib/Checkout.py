# create class
class Checkout:
    class Discount:
        def __init__(self, nbrItems, price):
            self.nbrItems = nbrItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
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

    # Add discount
    def addDiscount(self, item, nbrOfItems, price):
        discount = self.Discount(nbrOfItems, price)
        self.discounts[item] = discount

