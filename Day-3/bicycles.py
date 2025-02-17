bicycles = ['trek', 'canondale', 'redline', 'specialized']
print(bicycles)

# Lists are ordered collections. 
print(bicycles[0]) # Accessing the first element in a list

# Using string methods along with list
print(bicycles[0].title())
print(bicycles[0].lower())
print(bicycles[0].upper())

# Accessing last element from a list
print(bicycles[-1]) # index=-1 means last element, index=-2 means second last element etc..
# The above is also called Negative indexing

print(f"My first bicycle was a {bicycles[0].title()}")

