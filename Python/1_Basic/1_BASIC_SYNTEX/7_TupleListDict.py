# Data Types
# Number - Int / Float
# String - Str
# Boolean - True/False

# List - Like Array
fruits = ['apple', 'pear', 'banana']
print(fruits[1])        # choose seond one
fruits.append('melon')  # add 'melon' at the end of list
fruits.remove('pear')   # delete 'pear' if it is containded in list
fruits.pop()            # get last item and remove

list2 = list(range(-3, 5, 2))
print(list2)


sports = ['soccer', 'football', 'basketball']
for sport in sports:
    print(sport)
for i in range(0,3):        # range -> make tuple or list // range(first, last+1)
    print(sports[i])

# Tuple - Can not update
samsung = ('galaxy23', 'galaxy watch4', 'galaxy fold 3')
print(samsung)
# samsung.append('galaxy flip 4')

# Dictionary - key:value
weather = {'vancouver' : 'rain', 'seoul' : 'cold', 'washington' : 'cloudy'}
print(weather['vancouver'])
student = {'name' : ['minsoo', 'soohyun', 'yihyun'], 'address': ['vancouver', 'vancouver']}
print(student['name'][1])
