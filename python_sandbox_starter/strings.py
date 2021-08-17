# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods


name = 'Thisoora'
age = 27

# Concatenate
# print('Hello, my name is ' + name + ' and I am ' + str(age))


# String Formatting

# Arguments by position
# print('Hello, my name is {name} and I am {age}'. format(name=name, age=age))

# F-Strings (3.6+)
# print(f'Hello, my name is {name} and I am {age}')

# String Methods

s = 'hello world'

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lowercase
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count the no of a specific letter
sub = 'h'
print(s.count(sub))

# Starts with (boolean)
print(s.startswith('hello'))

# Ends with (boolean)
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric (boolean)
print(s.isalnum())

# Is all alphabetic (boolean)
print(s.isalpha())

# Is all numeric (boolean)
print(s.isnumeric())