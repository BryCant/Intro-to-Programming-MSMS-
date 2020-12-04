# 1) make a class called Vehicle. Initialize with number of wheels and number of doors.
# include a function to get the number of passengers.
# 2) add kwargs to the init function. kwargs to be anticipated are: headlights(bool), top_speed(int), passengers(list)
import random


class Vehicle:

    def __init__(self, wheels, door_num, color, **car_stuffs):
        self.wheels = wheels
        self.door_num = door_num
        self.color = color
        if car_stuffs is not None:
            if "headlights" in car_stuffs.keys():
                self.headlights = car_stuffs["headlights"]
            else:
                self.headlights = None
            if "top_speed" in car_stuffs.keys():
                self.top_speed = car_stuffs["top_speed"]
            else:
                self.top_speed = None
            if "passengers" in car_stuffs.keys():
                self.passengers = car_stuffs["passengers"]
            else:
                self.passengers = None
        else:
            self.car_stuffs = None

    def get_max_pass(self):
        if self.wheels == 2:
            return 2
        elif self.wheels > 2:
            return random.randint(4, 8)

    def get_driver_name(self):  # first passenger is driver
        return self.passengers[0]

    def honk(self):  # car go HONK!
        print("HONK!!" + "!" * self.wheels)
        return "HONK!!" + "!" * self.wheels


car = Vehicle(6, 4, "grey", headlights=False, top_speed=24, passengers=["Gracie", "Bryant", "Avery", "Keyan"])
car.honk()
print(f"Wheels: {car.wheels}, Doors: {car.door_num}, Color: {car.color}, Max Passenger: {car.get_max_pass()}")
print(f"PassengerInfo: {len(car.passengers)} passengers \n{car.passengers} and {car.get_driver_name()} is driving")
