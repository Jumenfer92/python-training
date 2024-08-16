# CSV LECTURA ESCRITURA
import csv

# escribir
with open("archivos/file.csv", "w") as archivo:
    writer = csv.writer(archivo)
    writer.writeroww(["twit_id"], "user_id", "text")
    writer.writerow([1000, 1, "primer twit"])
    writer.writerow([1001, 2, "segundo twit"])

# leer
with open("archivos/file.csv", "r") as archivo:
    reader = csv.reader(archivo)
    print(list(reader))
    archivo.seek(0)
    for linea in reader:
        print(linea)

with open("archivos/file.csv", "r") as r, open("archivos/temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if linea[0] == "1000":
            writer.writerow([1000, 1, "texto modificado"])
        else:
            writer.writerow(linea)
    os.remove("archivos/file.csv")
    os.rename("archivos/temp.csv", "archivos/archivo.csv")