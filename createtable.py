from connection import *

cur=conn.cursor()
cur.execute("DROP TABLE IF EXISTS Clip_ID")
table="""create table Clip_Id(
         No_pass int AUTO_INCREMENT,
        User_id varchar(255),
        Pass_id binary(133),
        Website_Name varchar(255),
        PRIMARY KEY(No_pass));"""
cur.execute(table)
print("Table is redy")