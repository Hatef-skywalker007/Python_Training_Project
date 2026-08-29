contacts = {}

while True:

    print("\n1. Add")
    print("2. Search")
    print("3. Delete")
    print("4. Show All")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":

        name = input("Name: ")
        number = input("Phone: ")

        contacts[name] = number

        print("Contact added!")

    elif choice == "2":

        name = input("Name: ")

        if name in contacts:
            print(contacts[name])
        else:
            print("Not found!")

    elif choice == "3":

        name = input("Name: ")

        if name in contacts:
            del contacts[name]
            print("Deleted!")

        else:
            print("Not found!")

    elif choice == "4":

        for name, number in contacts.items():
            print(name, ":", number)

    elif choice == "5":

        print("Goodbye!")
        break

    else:
        print("Invalid choice!")