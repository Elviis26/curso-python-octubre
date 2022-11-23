#  ==

color = "azul"
print(color == "azul")
print(color == "rojo")

# !=
print(color != "rojo")

# >
altura = 150
altura_min = 150
print(altura>altura_min)
#<
print(altura<altura_min)
# >=
print(altura>=altura_min)

precio = 100
IVA = 0.12
impuesto = precio * IVA
print(impuesto)

#<=

print(altura <= altura_min)

def abrir_puerta(altura,edad):
    altura_minima =150
    edad_minima =15
    edad_maxima=80

    if altura <= altura_minima:
        print("NO ALCANZA")
        return
    if edad <= edad_minima:
        print("MUY JOVEN")
        return
    if edad >= edad_maxima:
        print("MUY GRANDE")
        return

    print("PASE ADELANTE")


abrir_puerta(140,14)
