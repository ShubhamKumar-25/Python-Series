class Camera:
    def take_photo(self):
        print("Taking a photo...")

class musicPlayer:
    def play_music(self):
        print("Playing music...")

class smartPhone2(Camera, musicPlayer):
    pass

sp2 = smartPhone2()
sp2.take_photo()
sp2.play_music()

print("-----------------------------------------------------")


class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def drive(self):
        print("Car is driving...")

class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging...")

ecar = ElectricCar()
ecar.start()
ecar.drive()
ecar.charge()

print("--------------------------------")

class Animal:
    def eat(self):
        print("Animal is eating...")

class Dog(Animal):
    def bark(self):
        print("Dog is barking...")

class Cat(Animal):
    def meow(self):
        print("Cat is meowing...")

dog = Dog()
dog.eat()
dog.bark()

cat = Cat()
cat.eat()
cat.meow()


print("========================================")

class Camera:
    def take_photo(self):
        print("Taking a photo...")

class musicPlayer:
    def play_music(self):
        print("Playing music...")

class smartPhone2(Camera, musicPlayer):
    pass

sp2 = smartPhone2()
sp2.take_photo()
sp2.play_music()

# oops concept