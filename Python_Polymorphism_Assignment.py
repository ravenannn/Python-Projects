# parent class
# Declare properties
class Movies:
    director = "Unknown"
    release_year = 1999
    genre = "Unknown"
    lead_actors = []
    
    # Declare methods
    def buyTickets(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        print("Thank you, {}. You are being redirected to our ticketing site.".format(self.entry_name))

# child classes
class Superbad(Movies):
    director = "Greg Mottola"
    release_year = 2007
    genre = "Comedy"
    lead_roles = ["Michael Cera, Jonah Hill"]

    # Declare methods
    def buyTickets(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_age = input("Enter your age in years: ")
        if (int(entry_age) >= 18):
            print("Thank you. You are being redirected to our ticketing site.\nPlease remember to bring your ID for admittance into this adult-rated movie.")
        elif (int(entry_age) < 18):
            print("We're sorry. You are not old enough to view this adult-rated movie.")
        else:
            print("You did not enter a valid age")


class Frozen(Movies):
    director = "Jennifer Lee"
    release_year = 2013
    genre = "Children"
    lead_actors = ["Idina Menzel", "Kristen Bell", "Jonathan Groff", "Josh Gad"]





if __name__ == "__main__":
    ageRestricted = Superbad()
    ageRestricted.buyTickets()
    
