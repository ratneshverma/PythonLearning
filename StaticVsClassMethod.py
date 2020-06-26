class Number():
    def __init__(self, value):
        self.value = value
    @classmethod
    def sum(cls, value1, value2):
        return cls(value1+value2)
    """ @staticmethod
    def sum(value1, value2):
        return Number(value1+value2) """
    def print(self):
        print(str(self.value))

class Float(Number):
    # Skip defining an __init__ method, and it uses the same as Number
    # Skip defining the sum() method, and it uses the same as Number
    # Skip defining the print method, and it uses the same as Number
    # Or we could define our own print method for this class.
    def print(self):
        # Prints the number with 2 decimal places
        print("{:.2f}".format(self.value))


n = Number(0.15647)
n.print()
#0.15647
f = Float(0.15647)
f.print()
#0.15

f = Float.sum(0.11, 0.1593)
f.print()  # This should only print 2 decimal places!
#0.2693

