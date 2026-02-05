class SystemManager:
    """This class manages the hospital system display."""
    def __init__(self, hospital):
        self.hospital = hospital

    def display_all_patients(self) -> None:
        """Display all patients in the hospital."""
        print(f"\n--- Patient List: {self.hospital.name} ---")
        for dept in self.hospital.departments:
            for patient in dept.patients:
                print(patient.view_info())

    def display_all_staff(self) -> None:
        """Display all staff in the hospital."""
        print(f"\n--- Staff List: {self.hospital.name} ---")
        for dept in self.hospital.departments:
            for member in dept.staff:
                print(member.view_info())