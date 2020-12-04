# parent class
class Artwork:
    # assign values to properties
    def __init__(self, artist, medium, origin, completion_year, current_location):
        self.artist = artist
        self.medium = medium
        self.origin = origin
        self.completion_year = completion_year
        self.current_location = current_location
    
    # Declare method    
    def information(self):
        msg = "\nArtist: {}\nMedium: {}\nOrigin: {}\nCompletion Date: {}\nCurrent Location: {}".format(self.artist,self.medium,self.origin,self.completion_year,self.current_location)
        print(msg)


# child class instance

starryNight = Artwork("Vincent Van Gogh", "Oil Paint", "Saint-Remy-de-Provence, France", 1889, "The Museum of Modern Art - New York City, New York")



if __name__ == "__main__":
    starryNight.information()

    

    
