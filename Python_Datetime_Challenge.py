from datetime import datetime
import pytz

tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)
print("NY time:", datetime_NY.strftime("%H:%M"))
nyTime = datetime_NY.strftime("%H:%M")

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London time:", datetime_London.strftime("%H:%M"))
londonTime = datetime_London.strftime("%H:%M")

tz_Portland = pytz.timezone('America/Los_Angeles')
datetime_Portland = datetime.now(tz_Portland)
print("Portland time:", datetime_Portland.strftime("%H:%M"))
portlandTime = datetime_Portland.strftime("%H:%M")

openTimeStr = "09:00"
closeTimeStr = "17:00"


def allOpen():
    
    if (nyTime >= openTimeStr) & (nyTime < closeTimeStr):
        isNyOpen = "Open"
    else:
        isNyOpen = "Closed"

    if (londonTime >= openTimeStr) & (nyTime < closeTimeStr):
        isLondonOpen = "Open"
    else:
        isLondonOpen = "Closed"

    if (portlandTime >= openTimeStr) & (portlandTime < closeTimeStr):
        isPortlandOpen = "Open"
    else:
        isPortlandOpen = "Closed"



    print("The New York branch is {}. The London branch is {}. The Portland branch is {}.".format(isNyOpen, isLondonOpen, isPortlandOpen))


if __name__ == "__main__":
    allOpen()
