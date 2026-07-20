class Employee:
    def __init__(self,name,age,salary):

        if age <= 0:
            raise ValueError("Age must be positive.")

        if salary < 0:
            raise ValueError("Salary can't be negative.")

        self.name=name
        self.age=age
        self.salary=salary

    def __str__(self):
        return f'Employee {self.name} has age {self.age} and salary {self.salary}'
    


