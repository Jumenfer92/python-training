#FECHAS
import time
print(time.time())

from datetime import datetime
fecha1 = datetime(2023, 1, 1)
fecha2 = datetime(2023, 2, 1)

ahora = datetime.now()
print(ahora)

fechaStr = datetime.strftime
fechaStrp = datetime.strptime("2023-01-23", "%Y-%m-%d")

print(fecha.strftime("%Y.%m.%d"))
print(fecha1 > fecha2)

print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute
)