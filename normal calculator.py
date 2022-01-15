num_1 = float(input("Put your first number: "))
operator = input("Put your operator (+ - * /): ")
num_2 = float(input("Put your second number"))

if operator == "+":
    print ( num_1 + num_2 )
elif operator == "-":
    print (num_1 - num_2)
elif operator == "*":
    print (num_1 * num_2)
elif operator == "/":
    print (num_1 / num_2)
else:
    print("put right operator")
