from customer import Customer



print ("   M A I N - M E N U")
print ("1. Create Customer")
print ("2. View Customers")
print ("3. Action 3")
print ("4. Action 4")
print ("5. Action 5")

while True:
    # Get user input:
    choice = input('Enter a choice from the menu [1-5] : ')

    # Convert input (number) to int type:
    choice = int(choice)

    if choice == 1:
       print("Create Customer...")
       create_supplier()
    elif choice == 2:
        print ("Action 2...")
        #processing #2 is done here
    elif choice == 3:
        print ("Action 3...")
        #processing #3 is done here
    elif choice == 4:
        print ("Action 4...")
        #processing #4 is done here
    elif choice == 5:
        print ("Action 5...")
        #processing #5 is done here
    else:
        print ("Invalid entry. You should choose 1-5 only. Program exiting.....please restart it and try again.")
        # Add sys.exit() (will have to add 'import sys' to top





class Supplier(object):
    def __init__(self,number, name, address, phone_number, product):
        self.number = number
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.product = product

def create_supplier(self,number, name, address, phone_number, product):
    supplier_list = []
    number = input("Enter the supplier number:")
    print(number)
    name = input("Enter supplier name:")
    print(name)
    address = input("Enter the supplier's address:")
    print(address)
    phone_number = input("Enter the supplier's phone number:")
    print(phone_number)
    product = input("Enter the product they supply:")
    print(product)
    s = Supplier(number, name, address, phone_number, product)
    supplier_list.append(s) 

class Member(object):
    name = ""
    dob = ""
    gender = ""
    phone = ""
    address = ""


def __init__(self, name, dob,gender,phone, address):
    self.name = name
    self.dob = dob
    self.gender = gender 
    self.phone = phone
    self.address = address

members = []


def create_member(name, dob, gender,phone,address):
    name = input("Please enter your name -->")
    dob = input ("Please enter your dob -->")
    gender = input("Please eneter your gender -->")
    phone = input("Please eneter your phone -->")
    address = input("Please eneter your address -->")
    members.append(name,dob,gender,phone,address)