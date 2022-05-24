from Person import Person


class Employee(Person):
    def __init__(self, name: str, last_name: str, address: str, postal_code: str, phone_number: str, ssn: str, salary: int | float, department: str) -> None:
        super().__init__(name, last_name, address, postal_code, phone_number)
        self.salary = float(salary)
        self.ssn = ssn
        self.department = department

    def __str__(self) -> str:
        return f"""Name: {self.name}\nLastName: {self.last_name}\nAddress: {self.address}\nPostal/Zip Code: {self.postal_code}\nPhone Number: {self.phone_number}
        Salary: {self.salary}\nDepartment: {self.department}\nSSN: {self.ssn}"""
