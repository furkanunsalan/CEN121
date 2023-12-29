from question_3_customer import Customer

def main():
    customer = Customer("Jane", "124 Main Street", "555-1235", True, 12345)
    
    print("Person's Name: ", customer.name)
    print("Address: ", customer.address)
    print("Phone Number: ", customer.phone)
    print("Mail Preference: ", customer.mail)
    print("Customer Number: ", customer.customer_no)
    
main()
