# 1-9: Smartphone - 3+ states and behaviors
class Phone:
    def __init__(self, brand, model, battery=100):
        self.brand = brand
        self.model = model
        self.battery = battery
        self.is_on = False

    def turn_on(self):
        if self.battery > 0:
            self.is_on = True

    def turn_off(self):
        self.is_on = False

    def use_battery(self, amount):
        if self.is_on and amount >= 0:
            self.battery = max(0, self.battery - amount)
            if self.battery == 0:
                self.turn_off()

    def show_status(self):
        print(f"{self.brand} {self.model}; on={self.is_on}; battery={self.battery}%")

phone = Phone("Samsung", "Galaxy S26")
phone.show_status()
phone.turn_on()
phone.use_battery(15)
phone.show_status()
phone.turn_off()
phone.show_status()
