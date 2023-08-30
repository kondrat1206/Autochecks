class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        print("Meow")
        return "Meow"


class Dog(Animal):
    def say(self):
        print("Woof")
        return "Woof"
    

class CatDog(Cat, Dog):
    def info(self):
        result = f"{self.nickname}-{self.weight}"
        return result


class DogCat(Dog, Cat):
    def info(self):
        result = f"{self.nickname}-{self.weight}"
        return result

catdog = CatDog("aaa", 25)
catdog.say()
catdog.info()