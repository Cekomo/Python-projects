import csv

# aspect to be considered:
# code refactoring
# data validation like controlling if file is present
# performance issues like converting nested loop to while
# further error handling

class AddressBook:
    def __init__(self):
        self.register_count = 0
        self.calculate_register_count()

    def calculate_register_count(self):
        data = []
        self.register_count = len(self.read_file(data))

    def add_contact(self, name, email, phone_number):
        # user = {"Name": name, "E-mail": email, "Phone Number": phone_number}
        self.register_count += 1
        self.append_file(name, email, phone_number)
        print(f"User {name} is added to address book")
        # self.contacts.append(user)

    def view_contacts(self):
        i = 1
        data = []
        for entity in self.read_file(data):
            print(f"{i} - {entity}")
            # print(f"{i} - Name: {u['Name']} | E-mail: {u['E-mail']} | Phone Number: {u['Phone Number']}")
            i = i + 1

    def update_contact(self, old_name, name, email, phone_number):
        data = []
        i = 0
        entity_index = -1
        for entity in self.read_file(data):
            data[i] = entity

            if(entity[0] == old_name):
                data[i] = [name, email, phone_number]
                entity_index = i
                # entity.update({'Name': name, 'E-mail': email, 'Phone Number': phone_number})
                print(f"User {old_name} is updated.")
            i += 1
        
        if entity_index != -1:
            self.update_file(data)
        else:
            print("User cannot be updated because there is no user with this name.")
        
    def delete_contact(self, old_name):
        data = []
        i = 0
        entity_index = -1
        for entity in self.read_file(data):
            if(entity[0] == old_name):
                entity_index = i
                self.register_count -= 1
                continue

            data[i] = entity
            i += 1
        
        if entity_index != -1:
            self.update_file(data)
            print(f"User {old_name} is deleted.")
        else:
            print("User cannot be deleted because there is no user with this name.")

    def search_contact(self, name):
        i = 1
        data = []
        for entity in self.read_file(data):
            if(entity[0] == name):
                print(f"{i} - {entity}")
                return

            i += 1

        print(f"User {name} is cannot be found in address book.")

    def NavigateMenu(self):
        try:
            inpt = int(input("\nEnter a number to operate: "))
        except ValueError:
            print("Invalid character is typed.")
            self.NavigateMenu()

        if inpt == 1:
            name = input("Please enter a name: ")
            email = input("Please enter a E-mail: ")
            phone_number = input("Please enter a phone number (without country code): ")
            if (self.are_entities_validated(name, email, phone_number)):
                self.add_contact(name, email, phone_number)

        elif inpt == 2:
            self.view_contacts()

        elif inpt == 3:
            old_name = input("Please a user name: ")
            if self.is_name_valid(old_name):
                name = input("Please enter a name: ")
                email = input("Please enter a E-mail: ")
                phone_number = input("Please enter a phone number (without country code): ")
                if (self.are_entities_validated(name, email, phone_number)):
                    self.update_contact(old_name, name, email, phone_number)
            else:
                input("Please provide a valid user name.")
            
        elif inpt == 4:
            old_name = input("Please enter a name to delete the user: ")
            if self.is_name_valid(old_name):
                self.delete_contact(old_name)
            else:
                print("Please provide a valid user name.")

        elif inpt == 5:
            name = input("Please enter a name to find the user: ")
            if self.is_name_valid(name):
                self.search_contact(name)
            else:
                print("Searched user cannot be found")

        elif inpt == 0: # problem occurs when 0 is typed especially when an error occurs before
            print("Goodbye!\n")
            return

        else:
            print("Invalid character is typed.")

        self.NavigateMenu()

    def are_entities_validated(self, name, email, phone_number):
        if len(name) < 2 or not name.isalpha() or len(name) > 15:
            print("Name should have character count of 2-15 by only containing letters.")
            return False
        
        if '@' not in email or '.' not in email or '..' in email or len(email) < 7 or email[0] == '.' or email[0] == '@':
            print("Invalid E-mail.")
            return False
        
        if len(phone_number) != 10 or not int(phone_number.isdigit()) or phone_number[0] != '5': 
            print("Invalid phone number. The number must be like: 5*********")
            return False

        return True

    def save_entities(self, name, email, phone_number):
        return
    
    def append_file(self, name, email, phone_number):
        entity = [name, email, phone_number]
        with(open('address_book.csv', 'a', newline='')) as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(entity)

    def read_file(self, data):
        with open("address_book.csv", 'r',) as file:
            csvreader = csv.reader(file, delimiter=',')
            for entity in csvreader:
                data.append(entity)
            return data
    
    def update_file(self, data):
         i = 0
         with(open('address_book.csv', 'w', newline='')) as file:
            writer = csv.writer(file, delimiter=',')
            for entity in data:
                writer.writerow(entity)
                i += 1
                if (self.register_count <= i):
                    return
    
    def is_name_valid(self, old_name):
        with open("address_book.csv", 'r',) as file:
            csvreader = csv.reader(file, delimiter=',')
            for entity in csvreader:
                if (entity[0] == old_name):
                    return True  
                      
        return False
    
address_book1 = AddressBook()

print("Welcome to Address Book, please select a number that you would like to operate:")
print("1 - Add Contact\n2 - View Contacts\n3 - Update Contact\n4 - Delete Contact\n5 - Search Contact\n0 - Quit")
address_book1.NavigateMenu()