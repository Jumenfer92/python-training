# INVOCAR EXCEPTION
def division(n=0): #no se puede div por 0
    if n == 0:
        raise ZeroDivisionError("No dividas por 0", f"{n}")
    return 5 / n

try:
    division()
except ZeroDivisionError as e:
    print(e)
    