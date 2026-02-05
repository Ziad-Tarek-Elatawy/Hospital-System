from model.patient import Patient
from model.staff import Staff

class Department:
    """
    This class for hospital department, managing patients and staff
    """
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.staff = []

    def add_patient(self, patient: Patient) -> None:
        """
        Adds a patient to the department
        """
        self.patients.append(patient)

    def add_staff_member(self, staff: Staff) -> None:
        """
        Adds a staff member to the department
        """
        self.staff.append(staff)
        