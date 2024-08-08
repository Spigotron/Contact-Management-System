import re

def cms():
    while True:
        main_menu = input("""
                    
        Welcome to the Contact Management System!

        Main Menu:
                            
        1. Add a new contact
        2. Edit a contact
        3. Delete a contact
        4. Search for a contact
        5. Display all contacts
        6. Export all contacts to a text file
        7. Quit

        Enter a selection: """)

        if main_menu == "1":
            add_contact()
        elif main_menu == "2":
            edit_contact()
        elif main_menu == "3":
            delete_contact()
        elif main_menu == "4":
            find_contact()
        elif main_menu == "5":
            display_all_contacts()
        elif main_menu == "6":
            export_contacts()
        elif main_menu == "7":
            print("Thank you for using the Contact Management System. Have a nice day!")
            break
        else:
            print("Sorry, that is not a valid selection.")
            continue

contact_info = {
    123: 
        {"name": "Johnny Smith", 
        "phone": 123, 
        "email": "johnnysmith@gmail.com", 
        "address": "123 Dark Drive"},
    456:
        {"name": "Rachel Long", 
         "phone": 456, 
         "email": "rachellong@gmail.com", 
         "address": "456 Short Road"}
    }

def valid_email(email):
    pattern = r'[A-Za-z0-9_%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

    if re.match(pattern, email):
        return True
    else:
        return False
    
def add_contact():
    try:
        name_input = input("Enter name: ")
        phone_input = int(input("Enter phone number: "))
        email_input = input("Enter email address: ")
        address_input = input("Enter address: ")
    except ValueError:
        print("Sorry, that is not a valid phone number.")
        return
    
    if not valid_email(email_input):
        print("Sorry, that is not a valid email address.\n")
        return
    
    contact_info[phone_input] = {
                                    "name": name_input,
                                    "phone": phone_input,
                                    "email": email_input,
                                    "address": address_input
                                }
    print("Contact added!")
    return

def edit_contact():
    display_all_contacts()
    try:
        contact_input = int(input("Enter the phone number of the contact you would like to edit: "))
    except ValueError:
        print("Sorry, that is not a valid phone number.")
        return

    if contact_input in contact_info:

        try:
            name_input = input("Enter updated name: ")
            phone_input = int(input("Enter updated phone number: "))
            email_input = input("Enter updated email: ")
            address_input = input("Enter updated address info: ")
        except ValueError:
            print("Sorry, that is not a valid phone number.")
            return
        
        if not valid_email(email_input):
            print("Sorry, that is not a valid email address.\n")
            return
        
        contact_info.pop(contact_input)
        contact_info[phone_input] = {
                                        "name": name_input,
                                        "phone": phone_input,
                                        "email": email_input,
                                        "address": address_input
                                    }
        print("Contact updated!")
        return
    
    else:
        print("Sorry, there is no contact with that phone number.")

def delete_contact():
    display_all_contacts()
    contact_input = int(input("Enter the phone number of the contact you would like to delete: "))

    if contact_input in contact_info:
        contact_info.pop(contact_input)
        print("Contact deleted!\n")
        return
    else:
        print("Sorry, there is no contact with that phone number.")

def find_contact():
    try:
        phone = int(input("Enter the phone number of the contact you would like to find: "))
    except ValueError:
        print("Sorry, that is not a valid phone number.")

    contact = contact_info.get(phone, None)

    if contact is None:
        print("Sorry, there is no contact with that phone number.")
        return
    else:
        print(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n")

def display_all_contacts():
    if not contact_info:
        print("There are no contacts stored in the system.\n")
        return

    for contact in contact_info.values():
        print(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n")

def export_contacts():
    try:
        with open("contacts.txt", "w") as file:
            for contact in contact_info.values():
                file.write(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n\n")
    except Exception as e:
        print(f"Error: {e}")

    print("Contacts exported!\n")
    return

cms()