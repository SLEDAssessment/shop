from customer import Customer
#from supplier import Supplier
#from stock import Product
#from order import Order

def home_menu():
    print('HOME MENU')
    print('(1) Customer')
    print('(2) Supplier')
    print('(3) Product')
    print('(4) Generate Order')
    print('(5) Exit Navigation')
    
def input_number(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print('Response should not contain letters, please enter a numerical value.')
            continue
        else:
            return userInput
            break
      
def run_system():
    menu_choice = 1
    while menu_choice != 5:
        home_menu()
        menu_choice = input_number("Enter your choice(1-5) > ")
        while menu_choice > 5 or menu_choice < 1:
            menu_choice = input_number('Invalid option, please enter a value between 1 and 5 > ')
        if menu_choice == 1:
            customer_system()
        if menu_choice == 2:
            print('supplier in process')
            #supplier_system() 
        if menu_choice == 3:
            print('product in process')
            #product_system()
        if menu_choice == 4:
            print('order in process')
            #order_system()
        if menu_choice == 5:
            print('\nEXITING FROM SYSTEM')

def customer_menu():
    print('\nCUSTOMER MENU')
    print('(1) Create customer record')
    print('(2) View customer record')
    print('(3) Update customer details')
    print('(4) Delete customer record')
    print('(5) Back to home menu')
    
def customer_system():
    customer_choice = 1
    while customer_choice != 5:
        customer_menu()
        customer_choice = input_number("Enter your choice(1-5) > ")
        while customer_choice > 5 or customer_choice < 1:
            customer_choice = input_number('Invalid option, please enter a value between 1 and 5 > ')
        if customer_choice == 1:
            print('\nCREATE CUSTOMER RECORD:')
            Customer.create_customer()
        if customer_choice == 2:
            print('\nVIEW CUSTOMER RECORD:')
            Customer.view_customer()
        if customer_choice == 3:
            print('\nUPDATE CUSTOMER DETAILS:')
            Customer.update_customer()
        if customer_choice == 4:
            print('\nDELETE CUSTOMER RECORD:')
            Customer.delete_customer()
        if customer_choice == 5:
            print('\nRETURNING TO HOME MENU....\n')
    
#def supplier_menu():
#    print('SUPPLIER MENU')
#    print('(1) Create supplier record')
#    print('(2) View supplier record')
#    print('(3) Update supplier details')
#    print('(4) Delete supplier record')
#    print('(5) Back to home menu')
#    
#def supplier_system():
#    supplier_choice = 1
#    while supplier_choice != 5:
#        supplier_menu()
#        supplier_choice = input_number("Enter your choice(1-5) > ")
#        while supplier_choice > 5 or supplier_choice < 1:
#            supplier_choice = input_number('Invalid option, please enter a value between 1 and 5 > ')
#        if supplier_choice == 1:
#            print('\nCREATE SUPPLIER RECORD:\n')
#            Supplier.create_supplier()
#        if supplier_choice == 2:
#            print('\nVIEW SUPPLIER RECORD:\n')
#            Supplier.view_supplier()
#        if supplier_choice == 3:
#            print('\nUPDATE SUPPLIER DETAILS:\n')
#            Supplier.update_supplier()
#        if supplier_choice == 4:
#            print('\nDELETE SUPPLIER RECORD:\n')
#            Supplier.delete_supplier()
#        if supplier_choice == 5:
#            print('\nRETURNING TO HOME MENU....\n')
#    
#def product_menu():
#    print('PRODUCT MENU')
#    print('(1) Register product details')
#    print('(2) View product details')
#    print('(3) Update product details')
#    print('(4) Delete product details')
#    print('(5) Back to home menu')
#    
#def product_system():
#    product_choice = 1
#    while product_choice != 5:
#        product_menu()
#        product_choice = input_number("Enter your choice(1-5) > ")
#        while product_choice > 5 or product_choice < 1:
#            product_choice = input_number('Invalid option, please enter a value between 1 and 5 > ')
#        if product_choice == 1:
#            print('\nREGISTER PRODUCT DETAILS:\n')
#            Product.create_product()
#        if product_choice == 2:
#            print('\nVIEW PRODUCT DETAILS:\n')
#            Product.view_product()
#        if product_choice == 3:
#            print('\nUPDATE PRODUCT DETAILS:\n')
#            Product.update_product()
#        if product_choice == 4:
#            print('\nDELETE PRODUCT DETAILS:\n')
#            Product.delete_product()
#        if product_choice == 5:
#            print('\nRETURNING TO HOME MENU....\n')
#    
#def order_menu():
#    print('ORDER MENU')
#    print('(1) Create order')
#    print('(2) View order details')
#    print('(3) Update order details')
#    print('(4) Back to home menu')
#            
#def order_system():
#    order_choice = 1
#    while order_choice != 4:
#        order_menu()
#        order_choice = input_number("Enter your choice(1-5) > ")
#        while order_choice > 4 or order_choice < 1:
#            order_choice = input_number('Invalid option, please enter a value between 1 and 5 > ')
#        if order_choice == 1:
#            print('\nCREATE ORDER:\n')
#            Order.create_order()
#        if order_choice == 2:
#            print('\nVIEW ORDER DETAILS:\n')
#            Order.view_order()
#        if order_choice == 3:
#            print('\nUPDATE ORDER DETAILS:\n')
#            Order.update_order()
#        if order_choice == 4:
#            print('\nRETURNING TO HOME MENU....\n')
            
run_system()#runs full program              