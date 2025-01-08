class Animal:
    """Parent class for all animals on the farm."""

    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says {self.sound}."

    def eat(self, food):
        return f"{self.name} is eating {food}."

    def sleep(self):
        return f"{self.name} is sleeping."

    def __str__(self):
        return f"{self.name}, Age: {self.age}"


class Cow(Animal):
    """Child class for cows."""

    def __init__(self, name, age, milk_production):
        super().__init__(name, age, "Moo")
        self.milk_production = milk_production  # liters per day

    def produce_milk(self):
        return f"{self.name} produces {self.milk_production} liters of milk per day."


class Chicken(Animal):
    """Child class for chickens."""

    def __init__(self, name, age, eggs_per_day):
        super().__init__(name, age, "Cluck")
        self.eggs_per_day = eggs_per_day

    def lay_eggs(self):
        return f"{self.name} lays {self.eggs_per_day} eggs per day."


class Sheep(Animal):
    """Child class for sheep."""

    def __init__(self, name, age, wool_per_year):
        super().__init__(name, age, "Baa")
        self.wool_per_year = wool_per_year  # kilograms per year

    def shear(self):
        return f"{self.name} produces {self.wool_per_year} kg of wool per year."


# Example of how to use the classes
if __name__ == "__main__":
    # Create instances of animals
    bessie = Cow("Bessie", 5, 10)
    clucky = Chicken("Clucky", 2, 3)
    woolly = Sheep("Woolly", 4, 8)

    # Interact with the animals
    print(bessie)
    print(bessie.make_sound())
    print(bessie.eat("grass"))
    print(bessie.produce_milk())

    print()

    print(clucky)
    print(clucky.make_sound())
    print(clucky.eat("seeds"))
    print(clucky.lay_eggs())

    print()

    print(woolly)
    print(woolly.make_sound())
    print(woolly.eat("hay"))
    print(woolly.shear())
    