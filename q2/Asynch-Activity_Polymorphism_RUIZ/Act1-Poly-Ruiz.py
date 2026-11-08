class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount
    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        bill = self.__bill_amount * 1
        return bill

    def display_patient_type(self):
        return "Regular Patient"

class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.8 

    def display_patient_type(self):
        return "Senior Citizen"

class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85

    def display_patient_type(self):
        return "PhilHealth Member"

patient = Patient("Juan Dela Cruz", 15000)
seniorp = SeniorPatient("Maria Santos", 15000)
philhealthp = PhilHealthPatient("Pedro Reyes", 15000)

patients = [patient, seniorp, philhealthp]

print("\n Hospital Billing System")
print("------------------------\n")

for patient in patients:

    print(f"Patient Name: {patient.get_name()}")
    print(f"Patient Type: {patient.display_patient_type()}")
    print(f"Original Bill: ₱{patient.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{patient.calculate_bill():,.2f}\n")
