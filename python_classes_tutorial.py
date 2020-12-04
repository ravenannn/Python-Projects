
# Creating a class in Python
# Parent class User
class User:
    #Define the attributes of the class
    name = "No Name Provided"
    email = ""
    password = "1234abcd"
    account = 0
# Child classes inheriting properties and functions
class Employee(User):
    base_pay: 11.00
    department: 'General'

class Customer(User):
    mailing_address = ' '
    mailing_list = True



    #Define the methods of the class
    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page.")
                
    def __init__(self, name, email, password, account):
        self.name = name
        self.email = email
        self.password = password
        self.account - account


# ^^^^^For simplicity, this example is not using any security methods to
#encrypt the password. This is not how passwords would be handled in real use

# Outside of the class you would create an instance of the User class
# With this set up '__init__()', you can create a new object in a single line of code like this:

New_user = User("John Doe", "jdoe@outlook.com", "p@ssw0rd", 1234)




# Call the login method using the new object
New_user.login()
# Creating classes with arguments
