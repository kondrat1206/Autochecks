class Animal:

    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight
        

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, color):
        self.color = color


class Cat(Animal):

    def say(self):
        print("Meow")
        return "Meow"
    
class Dog(Animal):
        
    def __init__(self, nickname, weight, breed):
        self.breed = breed
        self.nickname = nickname
        self.weight = weight

    def say(self):
        print("Woof")
        return "Woof"

cat = Cat("Simon", 10)
dog = Dog("Barbos", 23, "labrador")
second_animal = Animal("Rikki", 4)
dog.say()
print(second_animal.color)
print(dog.breed, dog.nickname)

