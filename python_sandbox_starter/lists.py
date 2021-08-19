# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create List
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangoes')

# Remove from list
fruits.remove('Mangoes')

# Insert into a specific position
fruits.insert(2, 'Strawberries')

# Remove from a specifc position
fruits.pop(2)

# Change value
fruits[0] = 'Blueberries'

# Reverse the list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)