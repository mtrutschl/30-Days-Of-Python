# Day 2: 30 Days of Python Programming
first_name = 'Maya'
last_name = 'Trutschl'
full_name = 'Maya Trutschl'
country = 'USA'
city = 'Shreveport'
age = 18
year = 2026
is_married = False
is_true = True
is_light_on = True

first_name, last_name, full_name = 'Maya', 'Trutschl', 'Maya Trutschl'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))

if len(first_name) == len(last_name):
    print("Lengths are equal")
if len(first_name) > len(last_name):
    print("First name is longer")
if len(first_name) < len(last_name):
    print("Last name is longer")

num_one = 5
num_two = 4
total = (num_one + num_two)
diff = (num_one - num_two)
product = (num_one * num_two)
division = (num_one / num_two)
remainder = (num_two / num_one)
exp = (num_one ** num_two)
