class Counter:
  count = 0 # Class veriable
  def __init__(self):
    Counter.count += 1

  @classmethod
  def display_count(cls):
    print(f"Obrject Created {cls.count}")

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.display_count()
