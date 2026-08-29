try:

    number = int(input("Enter number: "))

    result = 10 / number

    print(result)

except ValueError:

    print("Please enter a number.")

except ZeroDivisionError:

    print("Cannot divide by zero.")