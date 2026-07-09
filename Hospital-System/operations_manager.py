from patient import Patient
from specialization import Specialization


class OperationsManager:
    def __init__(self):
        self.specializations = {}

        specialization_names = [
            "Cardiology",
            "Neurology",
            "Orthopedics",
            "Dentistry",
            "Pediatrics"
        ]

        for index, name in enumerate(specialization_names, start=1):
            self.specializations[index] = Specialization(name)

    def add_patient(self, specialization_number, name, age, status):
        patient = Patient(name, age, status)

        specialization = self.specializations.get(specialization_number)

        if specialization:
            specialization.add_patient(patient)
            print("Patient added successfully.")
        else:
            print("Invalid specialization.")

    def print_all_patients(self):
        for specialization in self.specializations.values():
            specialization.print_patients()

    def get_next_patient(self, specialization_number):
        specialization = self.specializations.get(specialization_number)

        if specialization:
            patient = specialization.get_next_patient()

            if patient:
                print(patient)
            else:
                print("No patients.")
        else:
            print("Invalid specialization.")

    def remove_patient(self, specialization_number, patient_name):
        specialization = self.specializations.get(specialization_number)

        if specialization:
            if specialization.remove_patient(patient_name):
                print("Patient removed successfully.")
            else:
                print("Patient not found.")
        else:
            print("Invalid specialization.")