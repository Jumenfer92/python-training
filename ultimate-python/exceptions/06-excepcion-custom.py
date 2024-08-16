# INVOCAR EXCEPTION CUSTOM

class MiError(Exception):
    "Mi exception personalizada"
    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo
    
    def __str__(self):
        return f"{self.mensaje} - codigo:{self.codigo} "

def division(n=0): #no se puede div por 0
    if n == 0:
        raise ZeroDivisionError("No dividas por 0", 805)
    return 5 / n

try:
    division()
except ZeroDivisionError as e:
    print(e)
    