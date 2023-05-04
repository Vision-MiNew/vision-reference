name = input("What's your name? : ")
print(f'Hello {name}')

adult_num = int(input("how many adult : "))
child_num = int(input("how many children : "))

def adult_price(adult_num):
    price = adult_num * 30
    print(f"Adult Price : {price}$")
    return price

def child_price(child_num):
    price = child_num * 12
    print(f"Children Price : {price}$")
    return price

total = adult_price(adult_num) + child_price(child_num)
print(f"Total Price : {total}$")
