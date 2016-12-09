class CashRegister():
    #This special method define the class constructor. There are we have 2
    #default values _itemCount and _totalPrice which are equal to 0.
    def __init__(self):
        self._itemCount = 0
        self._totalPrice = 0.0
        self._totalPounds = 0
    #This method add an item and add a price for this item.
    def addItem(self, price):
        self._itemCount = self._itemCount + 1
        self._totalPrice = self._totalPrice + price
    #This method return the total price of all items.
    def getTotal(self):
        return self._totalPrice
    #This method return the total number of all items.
    def getCount(self):
        return self._itemCount
    #Here I implemented a method getPounds that returns total price without
    #any pence (without float point)
    def getPounds(self, price):
        self._totalPrice = self._totalPrice + price
        self._totalPounds = int(self._totalPrice)
    #Here I implemented a method giveChange that returns change
    def giveChange(self, payment):
        self.payment = payment
        self.change = self.payment - self._totalPrice
    #This method resets the number of items and total price to default values,
    #which are equal 0.
    def clear(self):
        self._itemCount = 0
        self._totalPrice = 0.0

register1 = CashRegister()

register1.addItem(0.90)
register1.addItem(0.95)
register1.giveChange(10)

register2 = CashRegister()

register2.addItem(1.90)

a = [register1._itemCount, register1._totalPrice, register2._itemCount, register2._totalPrice, register1.change]
b = ["register1._itemCount", "register1._totalPrice", "register2._itemCount", "register2._totalPrice", "register1.change"]
c = dict(zip(b, a))
print (c)

