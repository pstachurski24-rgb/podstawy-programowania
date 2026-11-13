driving_mode = input("Enter driving mode (A/M/E): ")
distance = int(input("Enter distance in km: "))

if driving_mode == "A":
    fuel_consumption = 7
elif driving_mode == "M":
    fuel_consumption = 9
elif driving_mode == "E":
    fuel_consumption = 6
else:
    fuel_consumption = 0

total_consumption = distance / 100 * fuel_consumption

print(
    f"Total fuel consumption over {distance} km "
    f"in mode {driving_mode}: {total_consumption} liters"
)