from getpass import getpass

from connection import *
from keygen import *


def Save_pass():
 wname=input('Enter Website Name:')
 uname=input('Enter User Name:')
 password=getpass().encode()

 print("Are you sure you want save this data?\n")
 ch=input("Please enter Y if yes and N if no :")

 if ch == "N":
    print("You have chosen not to save any data\n")
    return() 

 elif ch == "Y":

   key=get_key()
   a=Fernet(key)
   encoded_pswd=a.encrypt(password)

   cur=conn.cursor()
   cur.execute("INSERT INTO Clip_Id (User_id, Pass_id, Website_Name) VALUES(?,?,?)",(uname,encoded_pswd,wname))
   conn.commit()

   print("Your Pasword has been saved")
   cur.execute("SELECT count(*) FROM clip_id")
   total=cur.fetchall()

   for row in total:
     for col in row:
        s1=col    
   print("Total number of passwords saved is:",(s1))
   return()
 elif(ch != "Y" or ch!= "N"):
   print("\nError: --Invalid choice-- \n")
   return()