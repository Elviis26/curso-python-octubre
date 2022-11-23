class Member:
    height = None
    imc = None
    name = None

    def __init__(self, name):
        self.name = name

    def register(self):
        print("USUARIO REGISTRADO")

    def welcome(self):
        print(f"Hola, bienvenido {self.name}")

    
elvis = Member("Elvis")
elvis.height = 165
elvis.imc = 15
print(elvis.height)
print(elvis.imc)
elvis.register()
elvis.welcome()

    #Herencia
class Person():
    first_name = None
    last_name = None
    birthdate = None



    def be_in_gym(self):
        print("ESTOY EN EL GIMNASIO")


class Trainer(Person):
    salary = None

    def be_in_gym(self):
        print("ESTOY TRABAJADO")

class Member(Person):
    imc = None

    def be_in_gym(self):
        print("ESTOY EJERCITANDOME")


alumno = Member()
alumno.be_in_gym()
#alumno.salary

from abc import ABC, abstractmethod

class Vehicule(ABC):
    doors = None
    wheels = None

    @abstractmethod
    def avanzar(self):
        pass

class Car(Vehicule):
    doors = 5
    wheels = 4

    def avanzar(self):
        return "AVANZO EN 4 RUEDAS"

class Bike(Vehicule):
    doors = 0
    wheels = 2

    def avanzar(self):
        print( f"AVANZO EN {self.wheels} RUEDAS")

    def __str__(self):
        return f"ESTA ES UNA MOTO CON {self.doors} puertas y {self.wheels} ruedas"

carro = Car()
print(carro.doors)

bike = Bike()
bike.avanzar()

print(bike)

class User():
    password = "contraseña-encriptada"

    def __init__(self) -> None:
        self.password = self.__decrypt()
    def __decrypt(self):
        return "contraseña-desencriptada"


usuario = User()
print(usuario.password)