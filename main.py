definitions = {}

while True:
    print("1: Add a definition")
    print("2: Find a definition")
    print("3: Delete a definition")
    print("4: Quit")

    choice = input("What would you like to do? ")

    if choice == "1":
        key = input("Enter the key (word) to define: ")
        definition = input("Enter the definition: ")
        definitions[key] = definition
        print("Definition added successfully")
    elif choice == "2":
        key = input("What are you looking for? ")
        if key in definitions:
            print(definitions[key])
        else:
            print("No definition found for", key)
    elif choice == "3":
        key = input("Which definition would you like to delete? ")
        if key in definitions:
            del definitions[key]
            print("Definition for", key, "deleted successfully")
        else:
            print("No definition found for", key)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid input")