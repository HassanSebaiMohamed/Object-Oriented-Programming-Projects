messages = [
    "1) Add new patient",
    "2) Print all patients",
    "3) Get next patient",
    "4) Remove a leaving patient",
    "5) End program"
]


def print_menu():
    for message in messages:
        print(message)


def input_is_valid(message, start, end):
    while True:
        try:
            number = int(input(message))

            if start <= number <= end:
                return number

            print(f"Please enter a number between {start} and {end}.")

        except ValueError:
            print("Invalid input. Please enter a number.")