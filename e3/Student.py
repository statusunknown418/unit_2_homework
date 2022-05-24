from Person import Person


class Student(Person):
    def __init__(self, name: str, last_name: str, address: str, postal_code: str, phone_number: str, career: str, grades_average: float) -> None:
        super().__init__(name, last_name, address, postal_code, phone_number)
        self.career = career
        self.grades_average = float(grades_average)

    def __str__(self) -> str:
        return super().__str__() + f"\nCareer: {self.career}\nGrades Average: {self.grades_average}"
