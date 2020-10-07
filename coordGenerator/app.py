import time

from csv import saveCSV
from fakeAddressGen import getFakePerson, PersonNotFromBsAsError, AddressNotFoundError

i = 1
limit = 400

while(i <= limit):

    try:
        person = getFakePerson()
        saveCSV(person)
        print(person)
        print("Persona nro: {}".format(i))
        i += 1
    except PersonNotFromBsAsError as e:
        print(e)
    except AddressNotFoundError as e:
        print(e)
    except IndexError:
        print("Error")
    finally:
        print("-------------------------")
        time.sleep(5)