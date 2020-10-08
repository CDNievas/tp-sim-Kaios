
import math, sys

def funcIP(x):
    try:
        return (1/0.8664123566450141)*(((math.pow(x,-0.37748))*(math.pow(563-x,1.4386)))/math.pow(563,2.06112))
    except ValueError as e:
        print("{}: en calculo IP".format(e))
        print("X= {}".format(x))
        sys.exit()

