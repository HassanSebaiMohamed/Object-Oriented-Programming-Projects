class utility:

    def input_positive_integer(self,message):
      while True:
        try:
            value = int(input(message))
            if value > 0:
                return value

            print("please enter a positive number")

        except ValueError:
            print("invalid input")

    def input_positive_float(self,message):
      while True:
        try:
            value = float(input(message))
            if value >= 0:
                return value

            print("salary can't be negative")

        except ValueError:
            print("invalid input")

    def input_is_valid(self,message, start, end):
     while True:
        try:
            choice = int(input(message))

            if start <= choice <= end:
                return choice

            print(f"Please enter a number from {start} to {end}.")

        except ValueError:
            print("Invalid input.")