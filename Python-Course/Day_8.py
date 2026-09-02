from abc import ABC, abstractmethod
# Inheritance in Python
# Single Inheritance
class Phone:
    def call(self):
        print("Calling....")

class SmartPhone(Phone):
    def internet(self):
        print("Browsing the internet...")

sp = SmartPhone()
sp.call()  
sp.internet()

print("------------------------------------------")

# Multiple Inheritance
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


print("------------------------------------------")

# Multilevel Inheritance
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

print("------------------------------------------")

# Hierarchical Inheritance
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


print("------------------------------------------")

# Hybrid Inheritance
class Device:

    def power_on(self):
        return "Power On"

class Speaker(Device):

    def sound(self):
        return "Sound playing"

class Display(Device):

    def show(self):
        return "Displaying video"

# Hybrid: Display + Speaker + Device
class SmartTV(Display, Speaker):
    pass

tv = SmartTV()
print(tv.power_on())  # Device se
print(tv.sound())  # Speaker se
print(tv.show())  # Display se

print("------------------------------------------")

# Encapsulation in Python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Private attribute:

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited: {amount}. New balance: {self.__balance}."

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew: {amount}. New balance: {self.__balance}."
        else:
            return "Insufficient balance."

    def get_balance(self):
        return f"Current balance: {self.__balance}."

acc = BankAccount(1000)
acc.deposit(1000)
acc.withdraw(500)
print(acc.get_balance())


print("------------------------------------------")

# Abstraction in Python
class Car(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class ElectricCar(Car):
    def start_engine(self):
        return "Electric car engine started silently."

class GasolineCar(Car):
    def start_engine(self):
        return "Gasoline car engine started with a roar."

class HybridCar(ElectricCar, GasolineCar):
    def start_engine(self):
        return "Hybrid car engine started with a combination of electric and gasoline power."


car = ElectricCar()
print(car.start_engine())

car2 = GasolineCar()
print(car2.start_engine())

car3 = HybridCar()
print(car3.start_engine())

print("------------------------------------------")

# polymorphism in Python

class UPIPayment:
    def pay(self, amount):
        return f"Paid {amount} pay using UPI Scanner."

class CardPayment:
    def pay(self, amount):
        return f"Paid {amount} pay using Card OTP."

class CashPayment:
    def pay(self, amount):
        return f"Paid {amount} pay using Cash, and received change."

def process_payment(payment_method, amount):
    print(payment_method.pay(amount))

upi = UPIPayment()
card = CardPayment()
cash = CashPayment()

process_payment(upi, 1000)
process_payment(card, 2000)
process_payment(cash, 500)