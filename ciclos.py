numero = 1

#while
while numero <=10:
    print(numero)
    numero+=1


perros = ["boby", "rex", "max","avellana"]

#for
for perro in perros:
    print(perro)

numero=1
while numero <=10:
    if numero ==5:
        break
    print(numero)
    numero+=1

perros = ["boby", "rex", "max", "avellana","max","max"]
for perro in perros:
    if perro=="max":
        print("este si es el perro")
        continue
    print("este no es el perro")