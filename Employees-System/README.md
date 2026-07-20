#  Employees Management System

A simple **Employees Management System** built with **Python** using **Object-Oriented Programming (OOP)** principles.

This project was created as an OOP practice project to improve class design, object interaction, and project organization.

---

##  Features

-  Add a new employee
-  Display all employees
-  Find an employee by name
-  Update an employee's salary
-  Delete employees within a specified age range
-  Input validation for ages, salaries, and menu choices

---

##  Technologies Used

- Python 3
- Object-Oriented Programming (OOP)

---

##  Project Structure

```
Employees-System/
│
├── employee.py
├── employees_manager.py
├── frontend_manager.py
├── utility.py
└── main.py
```

---

##  Class Diagram

### Employee

Represents an employee.

**Attributes**

- Name
- Age
- Salary

**Methods**

- `__init__()`
- `__str__()`

---

### EmployeesManager

Responsible for managing employees.

**Methods**

- Add Employee
- List Employees
- Find Employee by Name
- Update Salary
- Delete Employees by Age Range

---

### FrontendManager

Handles user interaction through a console menu.

**Responsibilities**

- Display menu
- Receive user input
- Call the appropriate manager functions

---

### Utility

Contains helper functions for validating user input.

**Functions**

- Positive Integer Validation
- Positive Float Validation
- Menu Choice Validation

---

##  How to Run

Clone the repository:

```bash
git clone https://github.com/HassanSebaiMohamed/Object-Oriented-Programming-Projects.git
```

Go to the project folder:

```bash
cd Object-Oriented-Programming-Projects/Employees-System
```

Run the program:

```bash
python main.py
```

---

##  Program Menu

```
1) Add a new employee
2) List all employees
3) Delete by age range
4) Update salary given a name
5) End the program
```

---

##  OOP Concepts Used

- Classes and Objects
- Encapsulation
- Object Composition
- Separation of Responsibilities
- Data Validation
- Modular Programming

---

## Example Output

```
Program Options:

1) Add a new employee
2) List all employees
3) Delete by age range
4) Update salary given a name
5) End the program

Enter your choice: 1

Enter employee name: Hassan
Enter employee age: 22
Enter employee salary: 10000

Employee added successfully.
```
--- 

##  Author

**Hassan Sebai**

