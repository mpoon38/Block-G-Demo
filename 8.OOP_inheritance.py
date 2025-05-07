# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the constructor of the parent class
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks.")

# Another derived class
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        print(f"{self.name} meows.")

# Using the classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Tabby")

dog.speak()  # Output: Buddy barks.
cat.speak()  # Output: Whiskers meows.
