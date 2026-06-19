class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def speak(self):
        print(self.sound)
        
class Dog(Animal):
    def __init__(self, name, sound, owner):
        super().__init__(name, sound)
        self.owner = owner

    def speak(self):
        print("Kêu")
        super().speak()
        
dog1 = Dog("Cay", "Gâu Gâu", "A")
dog2 = Dog("Chua", "Meo Meo", "B")
print(dog1.name)
dog1.speak()
print(dog2.name)
dog2.speak()