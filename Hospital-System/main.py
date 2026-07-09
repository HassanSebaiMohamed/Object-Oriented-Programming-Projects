from operations_manager import OperationsManager
from utility import print_menu, input_is_valid

manager = OperationsManager()

while True:
    print()

    print_menu()

    choice = input_is_valid("Choose: ", 1, 5)

    if choice == 1:
        specialization_number = input_is_valid(
            "Enter specialization number (1-5): ",
            1,
            5
        )

        name = input("Enter patient name: ")

        age = input_is_valid(
            "Enter patient age: ",
            1,
            120
        )

        status = input_is_valid(
            "Enter status (0 = Regular, 1 = Urgent): ",
            0,
            1
        )

        manager.add_patient(
            specialization_number,
            name,
            age,
            status
        )
        

    elif choice == 2:
        manager.print_all_patients()
        

    elif choice == 3:
        specialization_number = input_is_valid(
            "Enter specialization number (1-5): ",
            1,
            5
        )

        manager.get_next_patient(specialization_number)
        

    elif choice == 4:
        specialization_number = input_is_valid(
            "Enter specialization number (1-5): ",
            1,
            5
        )

        patient_name = input("Enter patient name: ")

        manager.remove_patient(
            specialization_number,
            patient_name
        )
        

    elif choice == 5:
        print("Program ended.")
        
        break