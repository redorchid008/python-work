# Sorting a list permanently with sort() method
cars = ['bmw', 'audi', 'mercedes', 'honda', 'hyundai', 'toyota']
print(f"Cars in original order: {cars}")

cars.sort()
print(f"Cars in alphabetical order: {cars}")

cars.sort(reverse=True)
print(f"Cars in reverse alphabetical order: {cars}")

print("###################################################################")
print("###################################################################")
# Sorting a list temporarily with sorted() method
cars = ['bmw', 'kia', 'mahindra', 'honda', 'mg', 'gmt']
print(f"Cars in original order: {cars}")

print(f"Cars in alphabetical order: {sorted(cars)}")
print(f"Cars in original order: {cars}")

print(f"Cars in reverse alphabetical order: {sorted(cars, reverse=True)}")
print(f"Cars in original order: {cars}")

print("###################################################################")
print("###################################################################")
# Sorting a list in a case-insensitive manner
bikes = ['honda', 'bajaj', 'BMW', 'R15', 'Ducati']

print(f"Alphabetical order: {sorted(bikes, key=str.lower)}")

print(f"Reverse Alphabetical order: {sorted(bikes, reverse=True, key=str.lower)}")
