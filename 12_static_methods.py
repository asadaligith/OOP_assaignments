class TemperatureConverter:
  @staticmethod    # staticmethod no need cls or self
  def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32   # formula convert celsius_temp into fahrenheit 

celsius = 25
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)

print(f"{celsius}°C is equal to {fahrenheit}°F")