#KWARGS keyword args
def getProduct(**datos):
    print(datos["id"], datos["name"])

getProduct(id="23",
           name="iPhone",
           desc="Xurria")
