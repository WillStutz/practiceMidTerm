'''Create two class definitions

1) a Play class that has attributes for
id, name, number of seats, date and status. Set the value of
the status attribute to True as default. Create an accessor
method each for the name, seats and status attributes only. 
Create a method called 'seats_left' that will reduce the 
number of seats by 1 every time it is called.
Create a mutator method called 'set_status' that will
change the status attribute to False.

2) a Booking class that has attributes for customer name and
seat number. Create accessor methods for both attributes.'''
        
class Play:

    def __init__(self,Id,name,numSeats,date):
        self.__status = True
        self.__id = Id
        self.__name = name
        self.__numSeats = numSeats
        self.__date = date

    def getName(self):
        return self.__name

    def getSeats(self):
        return self.__numSeats

    def getStatus(self):
        return self.__status

    def seatsLeft(self):
        if self.__numSeats >= 0:
            self.__numSeats = self.__numSeats - 1

    def get_seatsLeft(self):
        return self.__numSeats
    
    def set_status(self):
        self.__status = False

    def set_name(self, new_name):
        self.__name = new_name
    #danny method


class Book:

    def __init__(self,customerName,seatNumber):
        self.__customerName = customerName
        self.__seatNumber = seatNumber


    def getName(self):
        return self.__customerName
    
    def getSeat(self):
        return self.__seatNumber

    