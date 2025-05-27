def log_function_call(func):
  def wrapper():
    print("Function is being called before function executed")
    return func()
  return wrapper

@log_function_call   # decorator function
def say_hello():
  print("Hello")

say_hello()

