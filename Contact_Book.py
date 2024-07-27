import sys

def initial_phonebook():
    rows = int(input("Please enter initial number of contacts: "))
    cols = 3  # Adjusted to match the fields (name, number, email) in your example
    phone_book = []

    for i in range(rows):
        print("\nEnter contact %d details:" % (i+1))
        name = input("Enter name*: ")
        if not name.strip():
            sys.exit("Name is a mandatory field. Process exiting due to blank field...")
        
        number = int(input("Enter number*: "))
        email = input("Enter e-mail address: ")
        if not email.strip():
            email = None
        
        phone_book.append([name, number, email])

    return phone_book

def menu():
    print("\t\t\tSMARTPHONE DIRECTORY")
    print("You can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Update a contact")
    print("7. Exit phonebook")

    choice = int(input("Please enter your choice: "))
    return choice

def add_contact(pb):
    name = input("Enter name: ")
    number = int(input("Enter number: "))
    email = input("Enter e-mail address: ")

    pb.append([name, number, email])
    return pb

def remove_existing(pb):
    query = input("Please enter the name of the contact you wish to remove: ")
    removed = False

    for contact in pb[:]:  # Iterate over a copy of pb to avoid modifying it while iterating
        if query == contact[0]:
            pb.remove(contact)
            removed = True
            print(f"{query} has been successfully removed.")
    
    if not removed:
        print(f"Contact '{query}' not found.")

    return pb

def delete_all(pb):
    pb.clear()
    print("All contacts have been deleted.")
    return pb

def search_existing(pb):
    query_type = int(input("Enter search criteria:\n1. Name\n2. Number\n3. Email\nPlease enter: "))
    query = input("Please enter the search query: ")
    results = []

    for contact in pb:
        if query_type == 1 and query.lower() in contact[0].lower():
            results.append(contact)
        elif query_type == 2 and query == str(contact[1]):
            results.append(contact)
        elif query_type == 3 and query.lower() in str(contact[2]).lower():
            results.append(contact)
    
    if results:
        print("Search results:")
        display_all(results)
    else:
        print("No contacts found matching the search criteria.")

def update_contact(pb):
    query = input("Please enter the name of the contact you wish to update: ")
    updated = False

    for contact in pb:
        if query.lower() == contact[0].lower():
            print("Enter new details (leave blank to keep current):")
            new_name = input(f"Enter new name [{contact[0]}]: ")
            new_number = input(f"Enter new number [{contact[1]}]: ") or contact[1]
            new_email = input(f"Enter new e-mail address [{contact[2]}]: ") or contact[2]

            contact[0] = new_name if new_name else contact[0]
            contact[1] = int(new_number) if new_number else contact[1]
            contact[2] = new_email if new_email else contact[2]

            print(f"{query} has been successfully updated.")
            updated = True
    
    if not updated:
        print(f"Contact '{query}' not found.")

    return pb

def display_all(pb):
    if not pb:
        print("List is empty.")
    else:
        for contact in pb:
            print(contact)

def thanks():
    print("Thank you for using our Smartphone directory system.")
    print("Please visit again!")

def main():
    print("Hello dear user, welcome to our smartphone directory system")
    print("You may now proceed to explore this directory")
    
    pb = initial_phonebook()
    choice = 1

    while choice in (1, 2, 3, 4, 5, 6):
        choice = menu()

        if choice == 1:
            pb = add_contact(pb)
        elif choice == 2:
            pb = remove_existing(pb)
        elif choice == 3:
            pb = delete_all(pb)
        elif choice == 4:
            search_existing(pb)
        elif choice == 5:
            display_all(pb)
        elif choice == 6:
            pb = update_contact(pb)
        else:
            thanks()

if _name_ == "_main_":
    main()