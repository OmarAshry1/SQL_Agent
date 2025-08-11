import sqlite3
import streamlit as st
from langchain_groq import ChatGroq

## Connect to sqlite
connection= sqlite3.connect("student.db")
cursor = connection.cursor()

## create table
table_info="""

create table STUDENT (NAME VARCHAR(25),CLASS VARCHAR(25), SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

# Insert data
cursor.execute("INSERT INTO STUDENT (NAME,CLASS,SECTION,MARKS) VALUES ('Omar','Data Science','A',90)")
cursor.execute("INSERT INTO STUDENT (NAME,CLASS,SECTION,MARKS) VALUES ('Mohamed','Data Science','B',100)")
cursor.execute("INSERT INTO STUDENT (NAME,CLASS,SECTION,MARKS) VALUES ('Mostafa','DEVOPS','A',50)")
cursor.execute("INSERT INTO STUDENT (NAME,CLASS,SECTION,MARKS) VALUES ('Ashry','DEVOPS','A',30)")

## Display rec
print("Inserted data is: ")
data=cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)

##commit to db
connection.commit()
connection.close()