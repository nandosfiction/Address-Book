#new test
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database ='addressbook'
)

mycursor = mydb.cursor()

#add to database functions
def addContact():
    firstName = input('First Name: ')
    lastName = input('Last Name: ')
    number = input('Phone Number: ')
    emailAdd = input('Email Address: ')
    correct = input('are all the details correct? y/n ')
    if correct == 'y':
        sql = "INSERT INTO contacts (first_name, last_name, phone, email) VALUES (%s, %s, %s, %s)"
        val = (firstName, lastName, number, emailAdd)
        mycursor.execute(sql, val)
        mydb.commit()
    elif correct == 'n':
        addContact()
    else:
        print('Unrecognised Command, Resetting')

#create the remove function
def removeContact():
    #list all the sepcified entries
    firstName = input('Who do you want to remove? ')
    mycursor.execute("SELECT * FROM contacts WHERE first_name = %s", (firstName,))
    myresult = mycursor.fetchall()

    for result in myresult:
        print(result)

    #ask for the ID that match the name
    nameId = int(input('enter the number of the contact to remove: '))
    mycursor.execute("SELECT * FROM contacts WHERE id = %s", (nameId,))
    myresult = mycursor.fetchall()
    #print that out
    print('remove this entry?')
    print(myresult)
    #ask if they are sure
    yorn = input('y/n: ')

    if yorn == 'y':
        mycursor.execute("DELETE FROM contacts WHERE id = %s", (nameId,))
        mydb.commit()
        print('Entry has been deleted')
    else:
        callfunt()

#edit contacts
def editCon(conName):
    editDet = input('What do you want to edit? ')
    if editDet == 'number':
        newNum = input('Enter a new number: ')
        mycursor.execute("UPDATE contacts SET phone = %s WHERE first_name = %s", (newNum, conName,))
    elif editDet == 'first name':
        firstName = input('Enter a new first name: ')
        mycursor.execute("UPDATE contacts SET first_name = %s WHERE first_name = %s", (firstName, conName,))
    elif editDet == 'last name':
        lastName = input('Enter a new last name: ')
        mycursor.execute("UPDATE contacts SET last_name = %s WHERE first_name = %s", (lastName, conName,))
    elif editDet == 'email':
        email = input('Enter a new email address: ')
        mycursor.execute("UPDATE contacts SET email = %s WHERE first_name = %s", (email, conName,))
    else:
        print('UNLOWN COMMAND RESETTING')
        callfunt()

    print('Are you sure you want to change these details? ')
    changeDet = input('y/n: ')
    if changeDet == 'y':
        mydb.commit()
    else:
        callfunt()

#list all the contacts
def listAll():
    mycursor.execute("SELECT * FROM contacts ORDER BY first_name")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def callfunt():
    ask = input('what is it you would like to do? ')
    
    if ask == 'add':
        addContact()
    elif ask == 'remove':
        removeContact()
    elif ask == 'list':
        listAll()
    elif ask == 'edit':
        editCon(input('Who do you want to edit? '))
        
    #keep loop going until exit is called    
    while ask != 'exit':
        callfunt()
    else:
        quit()
callfunt()    