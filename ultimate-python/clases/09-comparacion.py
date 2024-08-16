#COMPARACION
class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

def __eq__(self, otro):
    return self.lat == otro.lat and self.lon == otro.lon

def __ne___(self, otro):
    return self.lat != otro.lat and self.lon != otro.lon

#menor que
def __lt__(self, otro):
    return self.lat + self.lon < otro.lat + otro.lon

#menor o igual
def __le__(self, otro):
    return self.lat + self.lon <= otro.lat + otro.lon

coords = Coordenadas(45, 34)
coords2 = Coordenadas(45, 34)

print(coords != coords2)
print(coords < coords2)