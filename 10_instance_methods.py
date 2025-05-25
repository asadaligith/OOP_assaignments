class Dog:
  def __init__(self, name, breed):
    self.name = name  # instance veriable
    self.breed = breed # instance veriable
    
    # instance method
  def bark(self):
    print(f"{self.name}, the {self.breed}, says: Woof! Woof!")

dog1 = Dog("Max", "Labrador") 
dog1.bark()
