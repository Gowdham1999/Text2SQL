import sqlite3 as sqlite

# Connect to sqlite database
connection = sqlite.connect('student.db')

# Creating cursor() function
cursor = connection.cursor() #cursor() is responsible for all actions which we are going to perform on the database

# Creating the table
table_info = """

create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INTEGER);

"""

cursor.execute(table_info)

# Now we will insert more records
cursor.execute("""insert into STUDENT values('Sam', 'Data Science', 'A', 90);""")
cursor.execute("""insert into STUDENT values('John', 'MBBS', 'B', 78);""")
cursor.execute("""insert into STUDENT values('Hari', 'Backend Dev', 'A', 99);""")
cursor.execute("""insert into STUDENT values('Steve', 'Maths', 'A', 77);""")
cursor.execute("""insert into STUDENT values('Daniel', 'Physics', 'B', 56);""")
cursor.execute("""insert into STUDENT values('Bruce', 'Chemistry', 'A', 33);""")
cursor.execute("""insert into STUDENT values('Kishan', 'Biology', 'B', 66);""")
cursor.execute("""insert into STUDENT values('Karthik', 'Social', 'A', 45);""")


# Displaying all the records
print("The records in STUDENT DB are")

student_records = cursor.execute("""select * from STUDENT;""")

for record in student_records:
   print (record) 

## Commit your changes int he databse
connection.commit()
connection.close()










