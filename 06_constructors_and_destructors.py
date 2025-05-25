class logger:
  def __init__(self, name):
    self.name = name

  def show_message(self):
    print(f"{self.name} object is Created")

  def __del__(self):
    print(f"{self.name} object is Destroyed")

massage = logger("Asad")
massage.show_message()

del massage
