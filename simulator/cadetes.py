cadetes = []

def getCadetes():
    return cadetes

def createCadetes(q):
    i = 0
    while(i<q):
        cadetes.append(Cadete(i))
        i += 1

def searchMinTC():
    cadetes.sort(key=lambda x: x.TC)
    return cadetes[0]

def calcTPOs(T):
    for cadete in cadetes:
        cadete.calcTPO(T)

class Cadete:

    id = 0
    TC = 0
    ITO = 0
    PTO = 0

    def __init__(self,id):
        self.id = id

    def setTC(self,T):
        self.TC = T

    def setITO(self, T):
        self.ITO = T 

    def calcTPO(self, T):
        self.PTO = self.ITO/T