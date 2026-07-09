class Patient:
    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status

    def __str__(self):
        if self.status == 1:
            patient_status = "Urgent"
        else:
            patient_status = "Regular"

        return f"Name: {self.name} | Age: {self.age} | Status: {patient_status}"