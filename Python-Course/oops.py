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