class Employee:
  def __init__(self, name, salary, ssn):
    self.name = name    # public veriable or attribute
    self._salary = salary # protected veriable or attribute
    self.__ssn = ssn      # private veriable

  def get_ssn(self):
    print("safe method to access private veriable")
    return self.__ssn

emp1 = Employee("Asad", 50000, 12345)  # object Created

print(emp1.name)
print(emp1._salary) # its used inside class and subclass.
# print(emp1.__ssn) ****not accessable direcly outside class, its given attribute error.****
print(emp1._Employee__ssn) # allow us via Name Mangling but its not best practice.

print(emp1.get_ssn()) # safe and recomanded way to access private veriable

