import sqlite3


#get personal data from user
##firstName = input("Enter your first name: ")
##lastName = input("Enter your last name: ")
##age = int(input("Enter your age: "))
##
###execute insert statement for supplied person data
##with sqlite3.connect('test_database.db') as connection:
##    c = connection.cursor()
##    line = "INSERT INTO People VALUES ('"+ firstName +"', '"+ lastName +"', " +str(age) +")"
##    c.execute(line)


## INSTEAD, use parameterized statements:
#get personal data from user
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age)

#execute insert statement for supplied person data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES(?, ?, ?)", personData)
    
    c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",
              (45, 'Luigi', 'Vercotti'))