class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
    
    def info(self):
        self.info = {}
        self.info["name"] = self.name
        self.info["age"] = self.age
        self.info["address"] = self.address
        return self.info

class Cat(Animal):

    def say(self):
        print("Meow")
        return "Meow"
    

class Dog(Animal):
    
    def __init__(self, nickname, weight, breed, owner):
        print(f'arg = {owner}')
        self.breed = breed
        self.owner = Owner(owner.name, owner.age, owner.address)
        #self.owner = owner
        
        
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        
        return self.owner.info()
        

#dog = Dog("Barbos", 23, "labrador")
#print(dog.who_is_owner())