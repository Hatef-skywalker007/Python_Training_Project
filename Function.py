#Simple function
def hello():
    print("Hello!")

hello()
# Parameter
def hello(name):
    print(f"Hello {name}")

hello("Ali")
hello("Sara")
# Return
def add(a, b):
    return a + b

result = add(10, 20)

print(result)