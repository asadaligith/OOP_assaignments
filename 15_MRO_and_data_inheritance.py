class A:
  def show(self):
    print("Method from class A")

class B(A):   # class B inherit from class A
  def show(self): # Method Override
    print("Method from class B")

class C(A):   # class C inherit from class A
  def show(self):     # Method Override
    print("Method from class C")

class D(B, C):  # inherit from B and C class
  pass

d1 = D()
d1.show()