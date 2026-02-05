from model.department import Department

class Hospital:
    def __init__(self, name: str, location: str):
        """Initializes the hospital with name and location."""
        self.name: str = name
        self.location: str = location
        self.departments: list[Department] = [] # List of Department objects

    def add_department(self, department: Department) -> None:
        """Adds a department to the hospital."""
        self.departments.append(department)