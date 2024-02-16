class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.sizes = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.sizes[carType-1]>0:
            self.sizes[carType-1] -= 1
            return True
        return False