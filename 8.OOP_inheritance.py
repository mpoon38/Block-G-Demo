# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived class
class Dog(Animal):
    def __init__(self, name, breed): #breed is the new attribute
        super().__init__(name)  # Call the constructor ( __init__ ) of the parent class
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks.")

# Another derived class
class Cat(Animal):
    def __init__(self, name, colour): #colour is the new attribute
        super().__init__(name)
        self.color = color

    def speak(self):
        print(f"{self.name} meows.")

# Using the classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Tabby")

dog.speak()  # Output: Buddy barks.
cat.speak()  # Output: Whiskers meows.
