# 1-6: Taxi - complete implementation based on assignment description
# NOTE: Original taxi.py was not provided; this is an independent implementation.
class Taxi:
    def __init__(self, distance_km, rate_per_km):
        self.distance_km = distance_km
        self.rate_per_km = rate_per_km

    def fare(self):
        return round(self.distance_km * self.rate_per_km, 2)

    def print_receipt(self):
        print("TAXI RECEIPT")
        print(f"Distance: {self.distance_km:.2f} km")
        print(f"Rate: {self.rate_per_km:.2f} PLN/km")
        print(f"Fare: {self.fare():.2f} PLN")
        print()

ride1 = Taxi(8, 3.5)
ride2 = Taxi(12.6, 4)
ride1.print_receipt()
ride2.print_receipt()
