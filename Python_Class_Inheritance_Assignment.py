
# Parent class

class Festival_Attendee:
    # Define attributes of the class
    name = "Name to be Provided"
    email = ""
    phone_number = "312-876-2140"
    festival_city = "Denver"


# Child classes
class Performer(Festival_Attendee):
    event_pay = 10,000
    manager_name = "No Name Provided"
    headliner = True

class Customer(Festival_Attendee):
    camping_pass = True
    vip_pass = False
    three_day_pass = True


