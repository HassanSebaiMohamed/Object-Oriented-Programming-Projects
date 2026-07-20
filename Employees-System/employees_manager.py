from employee import *

from utility import *

u = utility()

class EmployeesManager:

    def __init__(self):

        self.employees=[]

    def add_employee(self):

        print("\nenter employee info") 

        name = input("\nenter employee name") 

        age = u.input_positive_integer("\n enter employee age : ")

        salary = u.input_positive_float("\nenter employee salary : ")

        self.employees.append(Employee(name, age, salary))

    def  list_employees(self):
        if len(self.employees)==0:
            print("list is empty")
        else :
            for emp in self.employees:
                print(emp)

    def find_employee_by_name(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None
    
    def update_salary_by_name(self, name, salary):

        emp = self.find_employee_by_name(name)

        if emp is None:
            print('Error: No employee found')
        else:
            emp.salary = salary

    def delete_employees_with_age(self, age_from, age_to):

        for emp in self.employees[:]:

            if age_from <= emp.age <= age_to:

                print(f"Deleting employee {emp.name}")

                self.employees.remove(emp)