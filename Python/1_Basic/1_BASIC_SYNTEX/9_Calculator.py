# Conditional Statements

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

running = True

while running :

    print("-"*30)
    print(' [1] add \n [2] subtract \n [3] multiply \n [4] divide \n [exit] Quit')
    print("-"*30)

    select = input(" select mode : ")

    def calculate(select):
        num1 = float(input("first number : "))
        num2 = float(input("second number : ")) 
        
        if select == '1' :
            print(add(num1, num2))
        elif select == '2' :
            print(sub(num1, num2))
        elif select == '3' :
            print(mul(num1, num2))
        elif select == '4' :
            print(div(num1, num2))
        else:
            print("Error , Check your input")

    if select == 'exit':
        running = False
    else:
        calculate(select)


