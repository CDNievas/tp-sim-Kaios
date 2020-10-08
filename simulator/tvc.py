
import math, sys

def funcTVC(x):
    try:  
        return (1/1.91246)*((math.pow(x-0.49394,0.43288)*math.pow(105.07-x,0.426))/(math.pow(104.57606,0.85888)))
    except ValueError as e:
        print("{}: en calculo TVC".format(e))
        print("X= {}".format(x))
        sys.exit()
