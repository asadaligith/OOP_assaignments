class Engine :  # Engine Class
  def __init__(self, engine_type):
    self.engine_type = engine_type

  def start(self):
    print(f"The {self.engine_type} engine is starting") # Start Method

class Car :                          # Car Class
  def __init__(self, engine):
    self.engine = engine

  def start_engine(self):
    self.engine.start()           # used Engine Class start Method 


engine1 = Engine("V8")
car1 = Car(engine1)

car1.start_engine()
