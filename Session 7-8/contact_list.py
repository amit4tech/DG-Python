contacts = [("a", 123), ("b", 345), ("c", 567), ("d", 789), ("e", 102)]

name = input("Enter contact name:")
number = int(input("Enter phone number:"))

contact = (name, number)
contacts.append(contact)

print(contacts)

# for var in contacts:

    # if name == var[0]:
        # print("Phone number:", var[1])
    # print("Name:", var[0], "Contact:", var[1])