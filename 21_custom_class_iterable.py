import time

class Countdown:
    def __init__(self, start):
        self.start = start  # Store the start number
        self.current = start  # Set current counter

    def __iter__(self):
        return self  # The class itself is the iterator

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Stop when countdown is below 0
        value = self.current
        self.current -= 1  # Decrease the counter
        return value

# Test the Countdown in a for-loop
for number in Countdown(5):
    print(number)
    time.sleep(1)  # Delay for 1 second between iterations
