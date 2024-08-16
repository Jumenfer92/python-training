#utilidades.py

if __name__ != "__main__":
    from ..gestion.crud import guardar

    print(__name__)

    def pagar():
        print("realizando pago...")
        guardar()

    print("tarea de mantenimiento")

