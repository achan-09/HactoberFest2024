class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_count = 0

    def park_car(self):
        if self.current_count < self.capacity:
            self.current_count += 1
            print(f"Car parked. Current count: {self.current_count}")
        else:
            print("Parking lot is full!")

    def remove_car(self):
        if self.current_count > 0:
            self.current_count -= 1
            print(f"Car removed. Current count: {self.current_count}")
        else:
            print("Parking lot is empty!")

    def get_count(self):
        return self.current_count

# Example usage
if __name__ == "__main__":
    parking_lot = ParkingLot(capacity=5)  # Set the capacity of the parking lot

    parking_lot.park_car()
    parking_lot.park_car()
    parking_lot.remove_car()
    parking_lot.park_car()
    parking_lot.park_car()
    parking_lot.park_car()
    parking_lot.park_car()
    parking_lot.park_car()  # This should show that the lot is full
