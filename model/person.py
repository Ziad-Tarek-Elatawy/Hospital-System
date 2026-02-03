class Person:
    """
    Base class representing a person in the Hospital System.
    """
    
    def __init__(self, name: str, age: int) -> None:
        """
        Initializes the Person class with name and age.
        """
        if age < 0:
           raise ValueError("Age cannot be negative!")

        self.name = name
        self.age = age

    def view_info(self) -> str:
        """
        Returns person information as a string.
        """
        return f"Person Name: {self.name}, Age: {self.age}"
