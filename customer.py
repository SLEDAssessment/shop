class Customer:
    def __init__(self, name, phone, address, gender, industry):
        self.name = name
        self.phone = phone
        self.address = address
        self.gender = gender
        self.industry = industry

    def create_customer(self,name,phone,address,gender,industry):
        customers = []
        name = input('Enter your name: ')
        print(name)
        phone = input('Enter your phone number: ')
        print(phone)
        address = input('Enter your address: ')
        print(address)
        gender = input('Enter your gender: ')
        print(gender)
        industry = input('Enter your industry: ')
        print(industry)
        c = Customer(name, phone, address, gender, industry)
        customers.append(c)

