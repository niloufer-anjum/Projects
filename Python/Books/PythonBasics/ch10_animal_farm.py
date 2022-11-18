import random

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old. {self.gives_product()} {self.feed()} {self.speak()}"
    
    def gives_product(self, product):
        return f"{self.name} gave {random.randint(2,8)} {product} today!"

    def build_house(self, house):
        return f"{house} built for {self.name}"
    
    def feed(self, food):
        return f"{self.name} had {random.randint(1,5)} kilos of {food} today!"

    def speak(self, sound):
        return f"{self.name} says {sound}!"


class Cow(Animal):
    cow = {
        "sound": "Moo",
        "product": "gallons of milk",
        "food": "grass",
        "house": "Shed"
    }
    
    def speak(self, sound=cow["sound"]):
        return super().speak(sound)

    def gives_product(self, product=cow["product"]):
        return super().gives_product(product)
    
    def feed(self, food=cow["food"]):
        return super().feed(food)
    
    def build_house(self, house=cow["house"]):
        return super().build_house(house)
   
class Sheep(Animal):
    sheep = {
        "sound": "Baa",
        "product": "kilos of wool",
        "food": "grass",
        "house": "Pen"
    }

    def speak(self, sound=sheep["sound"]):
        return super().speak(sound)

    def gives_product(self, product=sheep["product"]):
        return super().gives_product(product)
    
    def feed(self, food=sheep["food"]):
        return super().feed(food)
    
    def build_house(self, house=sheep["house"]):
        return super().build_house(house)
   
class Chicken(Animal):
    chicken = {
        "sound": "cluck, cluck",
        "product": "dozens of eggs",
        "food": "grains",
        "house": "coop",
    }
    
    def speak(self, sound=chicken["sound"]):
        return super().speak(sound)

    def gives_product(self, product=chicken["product"]):
        return super().gives_product(product)
    
    def feed(self, food=chicken["food"]):
        return super().feed(food)
    
    def build_house(self, house=chicken["house"]):
        return super().build_house(house)


class Horse(Animal):
    def __str__(self):
        return f"{self.name} is {self.age} years old. {self.farm_hand()}"
    
    def farm_hand(self):
        return f"{self.name} pulled a cart today!"


millie = Cow("Millie", 4)
sheeple = Sheep("Sheeple", 2)
lola = Chicken("Lola", 1)
beauty = Horse("Black Beauty", 5)


print(millie)
print(sheeple)

# TODO: Doesn't override the food parameter
#lola.feed("oats")

print(lola)
print(beauty)