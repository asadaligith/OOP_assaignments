class Car:
  def __init__(self, brand):
    self.brand = brand

  def start(self):
    print(f"{self.brand} car started")

car1 = Car("Toyota")
car1.start()
