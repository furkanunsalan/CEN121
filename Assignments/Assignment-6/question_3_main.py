from question_3_customer import Customer

def main():
    customer = Customer("Jane", "124 Main Street", "555-1235", True, 12345)
    
    print("Person's name:", customer.name)
    print("mail preference:", customer.mail)
    print("Customer number:", customer.customer_no)
    

main()