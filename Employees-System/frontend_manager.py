from employees_manager import *

from utility import *

u = utility()

class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def print_menu(self):
        print("\nprogram options: ")
        messages = [
            '1) Add a new employee',
            '2) List all employees',
            '3) Delete by age range',
            '4) Update salary given a name',
            '5) End the program'
        ]  
        print('\n'.join(messages))

        msg = f"\nEnter your choice (1-{len(messages)}): "

        return u.input_is_valid(msg, 1, len(messages))
    
    def run(self):

     while True:

        choice = self.print_menu()

        if choice == 1:
            self.manager.add_employee()

        elif choice == 2:
            self.manager.list_employees()

        elif choice == 3:
            age_from = u.input_positive_integer("Enter age from: ")
            age_to = u.input_positive_integer("Enter age to: ")
            self.manager.delete_employees_with_age(age_from, age_to)

        elif choice == 4:
            name = input("Enter employee name: ")
            salary = u.input_positive_float("Enter employee salary: ")
            self.manager.update_salary_by_name(name, salary)

        elif choice == 5:
            print("Goodbye!")
            break

       
        


