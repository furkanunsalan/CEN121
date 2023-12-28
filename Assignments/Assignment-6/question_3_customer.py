from question_3_person import Person

class Customer(Person):
    def __init__(self, name, address, phone_number, mail:bool, customer_no:int):
        Person.__init__(self, name, address, phone_number)
        self.mail = mail
        self.customer_no = customer_no
    