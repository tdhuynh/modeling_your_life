
# Based on true events that happened this summer.


class Person:

    def __init__(self, name, happiness, bladder_meter, hangriness):
        self.name = name
        self.happiness = happiness
        self.bladder_meter = bladder_meter
        self.hangriness = hangriness

    def rest_up(self, trip):
        print("{} is taking a break so he doesn't go crazy!".format(self.name))
        self.happiness += 100

    def restroom_break(self, trip):
        print("{} needs to take a restroom break before hopping back on the road!".format(self.name))
        self.bladder_meter -= 100

    def food_time(self, trip):
        print("{} is getting food. He's not very friendly when he's hungry...".format(self.name))
        self.hangriness -= 30


class RoadTrip:

    def __init__(self, hours, location):
        self.hours = hours
        self.location = location

    def travel_time(self):
        self.hours -= 1
        person.happiness -= 25
        person.bladder_meter += 10
        person.hangriness += 10
        if self.hours == 0:
            print("Rejoice! {} has reached {}.".format(person.name, self.location))
        else:
            print("{} hours left until {} reaches {}!".format(self.hours, person.name, self.location))

person = Person("Tommy", 100, 0, 0)
trip = RoadTrip(18, "Eaux Claires Music Festival")

print("{}'s trip to {} will take {} hours.".format(person.name, trip.location, trip.hours))
while trip.hours != 0:
    trip.travel_time()
    if person.happiness == 0:
        person.rest_up(trip)
    if person.bladder_meter == 20 and trip.hours != 0:
        person.restroom_break(trip)
    if person.hangriness == 30:
        person.food_time(trip)
