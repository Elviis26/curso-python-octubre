
edad = 17


# if edad < 18:
#     raise Exception("ERES MENOR PARA USAR EL PROGRAMA")




class AgeException (Exception):
    pass

try:
    "texto" +5
    if edad<18:
        raise AgeException("Eres menor para usar el programa")
except Exception:
    print("se lanzo el error")