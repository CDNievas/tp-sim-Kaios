
fileRoute = "address.csv"

def saveCSV(person):
    f = open(fileRoute, "a")
    f.write(person.toCSV())
    f.close()