a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if a >= b and a >= c:
    print("A is the largest")

elif b >= a and b >= c:
    print("B is the largest")

else:
    print("C is the largest")