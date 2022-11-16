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

    



    #Herencia
    class Person():
        first_name = None
        last_name = None
        birthdate = None



        def be_in_gym(self):
            print("ESTOY EN EL GIMNASIO")


    class Trainer(Person):
        salary = None

    class Member(Person):
        imc = None

        def be_in_gym(self):
            print("ESTOY EJERCITANDOME")


    alumno = Member()
    alumno.be_in_gym()
    alumno.salary
