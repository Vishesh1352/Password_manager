from connection import *
from fatchdata import Fetch_data
from savepass import Save_pass
from createtable import *
from keygen import gen_key

print("Welcome to the Password Manager")
gen_key()
def manager():
    print("\nPlease Select")
    print("1.Get Password")
    print("2.Save Password")
    print("3.EXIT")

    sq= input("Plese enter your choice: ")
    if (sq == "1"):
        Fetch_data()
        manager()
    elif(sq == "2"):
        Save_pass()
        manager()
    elif(sq == "3"):
     conn.close()
    elif(sq != "1" or sq != "2" or sq != "3"):
        print("\nERROR: --- Plese enter a valid input ---\n")
        manager()
    else :
        manager()

manager()