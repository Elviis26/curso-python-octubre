def sumar():
        return 3+3
print("LA RESPUESTA ES: 5")

numero = sumar()


if numero == 5 :
        print("SI ES 5")
elif numero ==6:
        print("AH NO ERA UN 6")
else :
        print("NO ES UN 5")


x=0
while x<3:
        print(x)
        x+=1

print(range(3))

for i in range(3):
        print(i)


print("SEPARACION")
for i in range(3):
        if i ==1:
                continue
        print(i)
print("SEPARACION")
for i in range(3):
        if i ==1:
                break
        print(i)

print(True)
print(False)


print("SEPARACION")
def isAdult(edad):
        return edad >= 18


print(isAdult(15))
print(isAdult(20))


print(None)

def vacia():
        pass
print(vacia())

print(True and True)
print(True or True)
print(not  True)


if not isAdult(15):
        print("NO ES UN ADULTO")
