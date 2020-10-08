import random, sys

from cadetes import createCadetes, searchMinTC, calcTPOs, getCadetes
from ip import funcIP
from tvc import funcTVC


def runSimulation(CC,TF):

    # Variables internas del sistema
    T = 0
    TPLL = 0
    TP = 0

    # Variables auxiliares
    STPE = 0

    createCadetes(CC)

    return runIteration(T,TPLL,TP,STPE)

def printResults(CC,TP,cadetes,TPPE):

    print("Cantidad de Cadetes: {}".format(CC))
    print("Cantidad de entregas: {}".format(TP))

    print("Tiempo promedio desde pedido hasta entrega: {}".format(TPPE))

    print("% Ocioso por cadetes:")
    for cadete in cadetes:
        print("{}: {}".format(cadete.id,cadete.PTO))

def runIteration(T, TPLL, TP, STPE):

    T = TPLL
    IP = getIP()
    #print("STPE: {}".format(STPE))
    #print("IP: {}".format(IP))

    TPLL = T + IP
    TP = TP + 1
    TVC = getTVC()

    #print("TVC: {}".format(TVC))

    cadete = searchMinTC()
    
    #print("T: {}".format(T))

    if (T >= cadete.TC):

        cadete.setITO(cadete.ITO + T - cadete.TC)

        cadete.setTC(T + TVC)

        STPE = STPE + TVC

    else:

        cadete.setTC(cadete.TC + TVC)
        STPE = STPE + TVC +cadete.TC - T

    #print("Cadete: {} - {} - {}".format(cadete.id,cadete.TC,cadete.ITO))
    #print("STPE: {}".format(STPE))

    #print("---------------------------------")

    if T >= TF:
        
        calcTPOs(T)
        TPPE = STPE/TP

        return TP, getCadetes(), TPPE

    else:
        return runIteration(T,TPLL,TP,STPE)


def getIP():

    r1 = random.random()
    r2 = random.random()

    x = r1 * 563
    y = r2 * 0.128

    z = funcIP(x)
 
    if y <= z:
        return x
    else: 
        return getIP()

def getTVC():

    r1 = random.random()
    r2 = random.random()

    x = r1 * 87.55
    y = r2 * 0.32

    z = funcTVC(x)
 
    if y <= z:
        return x*2
    else:
        return getTVC()

if __name__ == "__main__":

    # Parametros
    CC = int(sys.argv[1])
    TF = int(sys.argv[2])

    TP, cadetes, TPPE = runSimulation(CC,TF)
    printResults(CC,TP,cadetes,TPPE)