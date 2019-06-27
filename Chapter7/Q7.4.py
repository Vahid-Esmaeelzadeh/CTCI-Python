import time


class Car:
    def __init__(self, plateNum: str):
        self.num = plateNum
        self.entranceTime = 0
        self.bill = 0
        self.pLot: ParkingLot = None

    def enter_request(self):
        self.pLot.new_car_request(self)

    def leave_request(self):
        self.pLot.car_leave_request(self)

    def pay_fee(self):
        self.bill = 0


class ParkingLot:
    def __init__(self, capacity=100, fee=5.00):
        self.capacity = capacity
        self.fee = fee
        self.cars = []

    def is_full(self):
        return len(self.cars) == self.capacity

    def new_car_request(self, c: Car) -> bool:
        if not self.is_full():
            self.cars.append(c)
            c.entranceTime = time.time()
            return True
        return False

    def car_leave_request(self, c: Car):
        dt = time.time() - c.entranceTime
        c.bill = (dt) * self.fee
        print("Your fee is", c.bill)
        c.pay_fee()

        if c.bill == 0:
            return True

        return False




parking1 = ParkingLot(10, 5)
car1 = Car("8BHY016")
car1.pLot = parking1

car1.enter_request()

time.sleep(10)

car1.leave_request()