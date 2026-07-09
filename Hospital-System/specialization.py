class Specialization:
    def __init__(self, name):
        self.name = name
        self.patients = []

    def add_patient(self, patient):
        if patient.status == 1:
            self.patients.insert(0, patient)
        else:
            self.patients.append(patient)

    def get_next_patient(self):
        if not self.patients:
            return None

        return self.patients.pop(0)

    def remove_patient(self, patient_name):
        for patient in self.patients:
            if patient.name.lower() == patient_name.lower():
                self.patients.remove(patient)
                return True

        return False

    def print_patients(self):
        print(f"\nSpecialization: {self.name}")

        if not self.patients:
            print("No patients.")
            return

        for patient in self.patients:
            print(patient)