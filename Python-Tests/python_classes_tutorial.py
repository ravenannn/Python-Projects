
# Creating a class in Python
# Parent class User
class User:
    #Define the attributes of the class
    name = "No Name Provided"
    email = ""
    password = "1234abcd"
    account = 0


    #Define the methods of the class
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("The password or email is incorrect")


# Child classes inheriting properties and functions
class Employee(User):
    base_pay = 11.00
    department = "General"
    pin_number = "3980"

    # This is the same method in the parent class
    # Instead of using entry_password, we are using entry_pin specific to employees
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}".format(self.name))
        else:
            print("The pin or email is incorrect")
    

class Customer(User):
    mailing_address = ' '
    mailing_list = True


# ^^^^^For simplicity, this example is not using any security methods to
#encrypt the password. This is not how passwords would be handled in real use

# Outside of the class you would create an instance of the User class
# With this set up '__init__()', you can create a new object in a single line of code like this:

##New_user = User()
##
##
### Call the login method using the new object
##New_user.login()
# Creating classes with arguments

# the following code invokes the methods inside each class for User and Employee
##customer = User()
##customer.login()

manager = Employee()
manager.getLoginInfo()
