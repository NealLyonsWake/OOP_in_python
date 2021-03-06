class Dog():

    def __init__(self, name, breed, age): 
       self.name = name
       self.breed = breed
       self.age = age

    def bark(self):
        return (f'{self.name} says Woof Woof')

    def dog_years(self,input=0):
        if not input:
            return (f'{self.name} is {self.age * 7} in dog years')
        else:
            return input * 7

    def species():
        return 'Canis lupus familiarise'


class TalkingDog(Dog):

    def __init__(self, name, breed, greet, age):
        super().__init__(name, breed, age)
        self.greet = greet

    def bark(self):
        return (f'{self.name} says {self.greet}')

    def __str__(self):
        return (f'Name: {self.name}, Breed: {self.breed}, Age: {self.age}')

    def __add__(self, other):
            return self.age + other.age
        

jasper = TalkingDog(name="Jasper", breed="Westy", greet="Hello", age=2)
whisper = TalkingDog(name="Whisper", breed="Sheep", greet="Hi", age=4)

print(jasper.dog_years())
print(jasper.bark())
print(whisper.bark())

print(whisper) # for use with __str__

hybridDog = jasper + whisper
print(hybridDog) # for use with __add__
