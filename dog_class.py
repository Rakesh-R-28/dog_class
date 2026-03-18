#class definition 
class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):
        print(f"Woof! My name is {self.name} and I'm a {self.breed}.")

# Creating the instance of the Dog class 
my_dog = Dog("Buddy", "Golden Retriever")
# Directing the dog to bark)
my_dog.bark()