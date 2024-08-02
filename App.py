import json

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactManager:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, contact):
        self.contacts.append(vars(contact))
        self.save_contacts()

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact['name'] == name:
                self.contacts.remove(contact)
                self.save_contacts()
                print(f"Removed {name} from contacts")
                return
            print(f"Contact {name} not found in contacts")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found")
        else:
            for contact in self.contacts:
                print(Contact(contact['name'], contact['phone'], contact['email']))

manager = ContactManager()
while True:
    print("\n1. Add Contact\n2. Remove Contact\n3. View Contacts\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter your name: ")
        phone = input("Enter your phone: ")
        email = input("Enter your email: ")
        contact = Contact(name, phone, email)
        manager.add_contact(contact)
    elif choice == '2':
        name = input("Enter name of contact to remove: ")
        manager.remove_contact(name)
    elif choice == '3':
        manager.view_contacts()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")