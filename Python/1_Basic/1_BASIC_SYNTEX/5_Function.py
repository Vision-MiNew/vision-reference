# def add_and_print (a, b, c) :   # a, b, c : parameters
#     result = a + b + c
#     print(result)

# x = 13.2
# y = 21.4
# z = 90

# add_and_print(x, y, z)         # x, y, z : arguments

def add_and_print (a, b, c) :   # a, b, c : parameters
    result = a + b + c
    return result

x = float(input('Enter first number : '))
y = float(input('Enter second number : '))
z = float(input('Enter third number : '))

print(add_and_print(x, y, z))        # x, y, z : arguments
