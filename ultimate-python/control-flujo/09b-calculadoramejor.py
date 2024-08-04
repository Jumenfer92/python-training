print("Calculadora 09")
print("Para salir escribe 'salir'")
print("Operaciones disponibles: suma, resta, multi y div")

resultado = None

while True:
    if resultado is None: 
        entrada = input("Introduce un número: ")
        if entrada.lower() == "salir":
            break
        try:
            resultado = float(entrada)
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")
            continue

    op = input("Ingresa operación: ")
    if op.lower() == "salir":
        break

    n2 = input("Introduce segundo número: ")
    if n2.lower() == "salir":
        break
    try:
        n2 = float(n2)
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")
        continue

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        if n2 == 0:
            print("No se puede dividir entre 0.")
            continue
        resultado /= n2
    else:
        print("Operación no válida")
        continue

    print(f"Resultado: {resultado}")
