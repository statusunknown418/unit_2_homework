from Employee import Employee


class Professor(Employee):

    def __init__(self, name: str, last_name: str, address: str, postal_code: str, phone_number: str, ssn: str, salary: int | float, department: str, is_member: bool) -> None:
        super().__init__(name, last_name, address, postal_code,
                         phone_number, ssn, salary, department)
        self.is_member = is_member

    def __str__(self):
        return super().__str__() + f"\nIs Member: {'Y' if self.is_member else 'N'}"
