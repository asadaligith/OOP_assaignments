from abc import ABC, abstractmethod
# Abstract Class
class Shape(ABC):
  @abstractmethod
  def area(self):
    pass
    
# inherit from Shape class
class Ractangale(Shape):
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width

ractangale1 = Ractangale(5, 6)
print("The rectangle area of ",ractangale1.area())