import practiceClass as p
import csv


shows = {
    "play1":{
        'id':3245,
        'name':'Phantom of the Opera',
        'capacity':65,
        'event_date':'03/01/2023'
    },
    "play2":{
        'id':1548,
        'name':'The Music Man',
        'capacity':45,
        'event_date':'05/15/2023'
    },
    "play3":{
        'id':9587,
        'name':'Hamilton',
        'capacity':124,
        'event_date':'07/21/2023'
    },
    "play4":{
        'id':6254,
        'name':'The Lion King',
        'capacity':89,
        'event_date':'09/29/2023'
    },

}

'''using the above dictionary iterate through it and create an instance of the 
play class that has id 9587
NOTE: Do not hard code the values to create the instance but use
keys and values from the dictionary '''

'''
for record in shows:
    if record == shows['play3']:
        Id = shows['play3']['id']
        name = shows['play3']['name']
        capacity = shows['play3']['capacity']
        event_date = shows['play3']['event_date']
'''

for record in shows:
    if shows[record]['id'] == 9587:
        the_play = p.Play(shows[record]['id'], shows[record]['name'],shows[record]['capacity'],shows[record]['event_date'])


#print(the_play.getName())



'''using the bookings.csv file process only those 
reservations for the same play (9587). Create an 
instance of the Booking class for each customer
that is going to play 9587 - Hamilton. 
if the play reaches capacity print out a 
error message as shown in output.JPG'''


#open the csv file in read mode

infile = open('bookings.csv','r')

#create a csv object from the file object from the step above

csvfile = csv.reader(infile)
next(csvfile)
# use a for loop to iterate through each record in the bookings file

for row in csvfile:
    if row[0] == '9587':
        the_customer = p.Book(row[1], row[2])
        the_play.seatsLeft()

        if the_play.get_seatsLeft() < 0:
            print('******** ERROR ********')
            print('Guest Name',the_customer.getName())
            print('Sorry, Show:',the_play.getName(),'is sold out')
            print('************************')
            print()

