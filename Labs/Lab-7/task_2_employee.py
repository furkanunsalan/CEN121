class Employee:
    
    def __init__(self, name, id, department, job_title):
        self.name = name
        self.id = id
        self.department = department
        self.job_title = job_title
    
    # Setters are useless in this case, but I wrote them anyway.
    def set_name(self, name):
        self.name = name
        
    def set_id(self, id):
        self.id = id
        
    def set_department(self, department):
        self.department = department
    
    def set_job_title(self, job_title):
        self.job_title = job_title
        
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id

    def get_department(self):
        return self.department
    
    def get_job_title(self):
        return self.job_title
    
    # Another option is to use __str__ method and write the table in the class itself and print Employee.result in main().

