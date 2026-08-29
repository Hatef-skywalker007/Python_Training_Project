contacts = {
    "Ali": "0912",
    "Sara": "0935",
    "Reza": "0911"
}

print(contacts["Ali"])

print(contacts)

contacts["Mohammad"] = "0990"
#Delete a contact
del contacts["Reza"]
#pop
for name, number in contacts.items():
    print(name, number)