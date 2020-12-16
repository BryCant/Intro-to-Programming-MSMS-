import random


class Student:
    def __init__(self, name, age, glasses, volume, nag_level):
        self.name = name
        self.age = age
        self.glasses = glasses
        self.volume = volume
        self.nag_level = nag_level

    def __str__(self):
        return f"Hi I am {self.name} and I am {self.age} years old {'!' * self.volume}"


class Vehicle:
    def __init__(self, wheels, door_num, color, **car_stuffs):
        self.wheels = wheels
        self.door_num = door_num
        self.color = color
        if car_stuffs is not None:
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

    def __str__(self):  # car go HONK!
        print("HONK!!" + "!" * self.wheels)
        return "HONK!!" + "!" * self.wheels


class SchoolBus(Vehicle):
    def __init__(self, wheels=4, door_num=2, color="yellow", **car_stuffs):
        super().__init__(wheels, door_num, color, **car_stuffs)
        self.bus_num = random.randint(100,999)

    def get_max_pass(self):
        return random.randint(len(self.passengers), len(self.passengers) + 12)

    def __add__(self, other):
        if type(other) == SchoolBus:
            self.passengers, other.passengers[:] = (self.passengers[:] + other.passengers), []
            return f"Passengers on Bus #{other.bus_num} have moved to Bus #{self.bus_num}"
        elif type(other) == Student:
            self.passengers = self.passengers[:] + [other.name]
            return f"{other.name} (student) is now on Bus #{self.bus_num}"
        else:
            print("Operation unsuccessful. Verify compatible types.")


keyan = Student("Keyan", 17, True, 7, 10)
ewingBus = SchoolBus(top_speed=90, passengers=["Ewing", "Bryant", "Avery", "Blake", "Hayden"])
jordanBus = SchoolBus(top_speed=90, passengers=["Jordan", "Other Jordan", "Jayden", "Aaron", "Natalie"])
print(ewingBus + keyan)
print(ewingBus.passengers)
print(ewingBus + jordanBus)
print(ewingBus.passengers)
