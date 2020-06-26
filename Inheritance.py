class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self, str):
        print(f'{self.name} Speak: {str}')

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def GetAge(self):
        print(f'Age:{self.age}')


class Cat(Animal):
    def fun1(self):
        print('jh')


c = Cat('holo')
c.fun1()
c.speak('Meow')

b = Dog('Rob', 5)
b.speak('Woo')
b.GetAge()
print(isinstance(b,Animal))
print(b.__dir__())
print(Dog.mro())