from task_2_employee import Employee

def main():
    # Create the employees.
    employee_1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    employee_2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    emplolyee_3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
    
    # Print the table.
    print("Name\t\tID Number\tDepartment\tJob Title")
    print("--------------------------------------------------")
    print(f"{employee_1.get_name()}\t{employee_1.get_id()}\t\t{employee_1.get_department()}\t{employee_1.get_job_title()}")
    print(f"{employee_2.get_name()}\t{employee_2.get_id()}\t\t{employee_2.get_department()}\t\t{employee_2.get_job_title()}")
    print(f"{emplolyee_3.get_name()}\t{emplolyee_3.get_id()}\t\t{emplolyee_3.get_department()}\t{emplolyee_3.get_job_title()}")
    print("--------------------------------------------------")
    
main()
