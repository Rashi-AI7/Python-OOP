name = input("Enter your name: ")
age = int(input("Enter your age: "))
date = (input("Enter the date of departure(dd/mm/yy): "))
depart_loc = input("Enter the departure location: ")
arrival_loc = input("Enter the arrival location: ")

class Train:
    def __init__(self, name, age, date, depart_loc, arrival_loc):
        self.name = name
        self.age = age
        self.date = date
        self.departurelocation = depart_loc
        self.arrivallocation = arrival_loc

    def ticket_info(self, ):
        print(f"Passenger name {self.name}")
        print(f"Passenger age {self.age}")
        print(f"Date {self.date}")
        print(f"Departing Loaction {self.departurelocation}")
        print(f"Arriving Location {self.arrivallocation}")

    def get_status(self, trainno, berth, coach, fare):
        self.train_num = trainno
        self.berth = berth
        self.coach = coach
        self.fare = fare
        print(f"Train number: {self.train_num}")
        print(f"Berth: {self.berth}")
        print(f"Coach: {self.coach}")
        print(f"Fare: {self.fare}")

p1 = Train(name, age, date, depart_loc, arrival_loc)
p1.get_status(12635, "Upper Berth", "s1", 200)
