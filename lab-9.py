class Car:
    def __init__(self, manufacturer, model, year, color, fuel_type):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = fuel_type
        self.is_running = False
    
    def start(self):
        if not self.is_running:
            self.is_running = True
            print("The car is now running.")
        else:
            print("The car is already running.")
    
    def stop(self):
        if self.is_running:
            self.is_running = False
            print("The car has been stopped.")
        else:
            print("The car is already stopped.")
    
    def carDetails(self):
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Fuel Type: {self.fuel_type}")

my_car = Car("Toyota", "Camry", 2022, "Black", "Gasoline")
my_car.carDetails()
my_car.start()
my_car.stop()
