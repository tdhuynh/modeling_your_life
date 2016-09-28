
class Person:

    def __init__(self, name, happiness):
        self.name = name
        self.happiness = happiness

    def rest_up(self, trip):
        print("{} is taking a break so he doesn't go crazy!".format(self.name))
        self.happiness += 100

    def bathroom_break(self, trip):
        print(" ")


class RoadTrip:

    def __init__(self, hours, location):
        self.hours = hours
        self.location = location

    def add_driver(self, person):
        self.drivers.append(person)

    def travel_time(self):
        self.hours -= 1
        person.happiness -= 25
        if self.hours == 0:
            print("Rejoice! {} has reached {}.".format(person.name, self.location))
        else:
            print("{} hours left until {} reaches {}!".format(self.hours, person.name, self.location))

person = Person("Tommy", 100)
trip = RoadTrip(18, "Eau Claire, WI")

print("{}'s trip to {} will take {} hours.".format(person.name, trip.location, trip.hours))
while trip.hours != 0:
    trip.travel_time()
    if person.happiness == 0:
        person.rest_up(trip)
