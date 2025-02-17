# Modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)


# Appending element to the end of a list
motorcycles.append('BMW')
print(motorcycles)

cars = []
cars.append('honda')
cars.append('hyundai')
cars.append('kia')
print(cars)
print(cars[0].upper())


# Inserting elements into a list
cars.insert(2, 'mahindra')
print(cars)


# Removing elements from a list
# Using del statement - if we know the index position of the item which needs to be removed
motorcycles = ['honda', 'yamaha', 'bajaj', 'bmw']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# Using pop() method
motorcycles = ['honda', 'yamaha', 'bajaj', 'bmw', 'ducati']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
popped_motorcycle = motorcycles.pop(2)
print(motorcycles)
print(popped_motorcycle)


# Using remove() method
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)