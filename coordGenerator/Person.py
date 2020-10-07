class Person:

    def __init__(self, name, street, city, state, coordLat, coordLong):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.lat = coordLat
        self.long = coordLong

    def __str__(self):
        return "Nombre: {}\nCalle: {}\nCiudad: {}\nProvincia: {}\nLatitud: {}\nLongitud: {}".format(self.name,self.street,self.city,self.state,self.lat,self.long)

    def toCSV(self):
        return "{},{},{},{},{},{}\n".format(self.name,self.street,self.city,self.state,self.lat,self.long)
