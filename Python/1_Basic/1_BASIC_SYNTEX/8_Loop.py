# while - Conditional

x = 1
running = True
while running:              # escape ?
    x += 1                  # x = x + 1
    print(x)
    if x > 10:
        running = False

x = 1
while True:              # escape ?
    x += 1               # x = x + 1
    print(x)
    if x > 10:
        break

list1 = []
list1.append('hello')
fruits = ['banana', 5.85 , 'Grape']
list2 = list(range(-3, 5, 2))
print(list2)

for fruit in range(1,8):
    print(fruit)
