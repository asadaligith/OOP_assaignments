class Person:
  def __init__(self, name):
    self.name = name

class Teacher(Person):
  def __init__(self, name, subject):
    super().__init__(name)
    self.subject = subject

teacher1 = Teacher("Asad", "Python")

print(teacher1.name)
print(teacher1.subject)