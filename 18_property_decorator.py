class Product:
  def __init__(self, price):
    self._price = price

  @property
  def price(self):
    return self._price

  @price.setter
  def price(self, new_price):
    if new_price < 0:
      raise ValueError("Price cannot be negative")
    self._price = new_price

  @price.deleter
  def price(self):
    print("Price deleted")
    del self._price

product1 = Product(100)
print(product1.price)

product1.price = 150
print(product1.price)