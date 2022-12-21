import pyperclip

from connection import *
from keygen import *


def Fetch_data():
    webname=input('Please Enter Website Name:')
    username=input('Plese Enter User Name:')
    cur=conn.cursor()
    cur.execute("SELECT Pass_id FROM Clip_Id WHERE Website_Name LIKE ? AND User_id LIKE ?",(webname,username))
    rows=cur.fetchall()
   
    if len(rows)== 0 :
        print("\n ERROR: ---There is no such website in the Database ---\n")
        Fetch_data()
    else:    
    
     for row in rows:
      for col in row:
         s1=col    
     key=get_key()
     b= Fernet(key)
     decode_s1=b.decrypt(s1)
     ssr=str(decode_s1)
     ln=len(ssr)-1
     ssr=ssr[2:ln]
     pyperclip.copy(ssr)
     print("\nYour password has been copied to clipboard Use Ctr+V to paste it.\n")
    return()