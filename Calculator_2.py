a = float(int(input(" First Number : ")))
b = float(int(input(" second Number : ")))

operator = input("choose(+,-,* , /):")

if operator == "+":
    print( a + b)
elif operator == "-":
    print( a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    if b != 0:
        print(a / b)
    else:
        print("cannot divide by zero")
else:
    print("invalid syntax")


#if,elif,else oprator

