class Person:
    def __init__(self, name: str, last_name: str, address: str, postal_code: str, phone_number: str) -> None:
        self.name = name
        self.last_name = last_name
        self.address = address
        self.postal_code = postal_code
        self.phone_number = phone_number

    def __str__(self) -> str:
        return f"Name: {self.name}\nLastName: {self.last_name}\nAddress: {self.address}\nPostal/Zip Code: {self.postal_code}\nPhone Number: {self.phone_number}"
