class Foo():
    def __init__(self):
        self._bar = 3

    @property
    def bar(self):
        return self._bar

    @bar.setter
    def bar(self, bar):
        self._bar = bar


obj = Foo()
obj1 = obj
print(obj.bar)
print(obj1.bar)
obj.bar = 10
print(obj.bar)
print(obj1.bar)
