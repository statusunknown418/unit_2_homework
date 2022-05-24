import pandas

from Employee import Employee
from Professor import Professor
from Student import Student

regular_employees = []

professors = []

students = []


def quit_program(groups: list[list] = []):
    if len(groups) == 0:
        print("Program exited successfully!")
        exit()

    df = pandas.DataFrame(columns=["Name", "Last Name", "Address", "Postal/Zip Code",
                          "Phone Number", "SSN", "Salary", "Department", "Is Member"])

    # Merge all groups into one dataFrame
    for group in groups:
        df = df.append(pandas.DataFrame(group, index=[0]))

    print("Report generated:")
    print(df)

    df.to_csv("report.csv", index=False)
    exit()


def employee_options():
    return {
        "name": input("Name: "),
        "last_name": input("Last Name: "),
        "address": input("Address: "),
        "postal_code": input("Postal/Zip Code: "),
        "phone_number": input("Phone Number: "),
        "ssn": input("SSN: "),
        "salary": input("Salary: "),
        "department": input("Department: "),
    }


def professor_options():
    options = employee_options()
    return {
        **options,
        "ssn": input("SSN: "),
        "salary": input("Salary: "),
        "department": input("Department: "),
        "is_member": input("Is Member: Y/N").upper() == "Y",
    }


def student_options():
    options = employee_options()
    return {
        **options,
        "career": input("Career: "),
        "grades_average": input("Grades Average: "),
    }


# The option `keys` are not in English (doesn't follow good practices) because that's what's asked
OPTIONS = {
    "EM": (regular_employees, Employee, 4, employee_options),
    "D": (professors, Professor, 3, professor_options),
    "E": (students, Student, 7, student_options),
}


def recursive_run():
    # This recursive function allow us to run the program until its exited without using a `while`
    try:
        option = input("\nChoose an option: \n"
                       "E: Employees\n"
                       "D: Professors\n"
                       "E: Students\n"
                       "S: Quit\n"
                       "> ").upper()

        if option == "S":
            quit_program()

        if option not in OPTIONS:
            raise ValueError

        selected_group_tuple = OPTIONS[option]

        if len(selected_group_tuple[0]) > selected_group_tuple[2]:
            raise Exception("The group is full")

        selected_group_tuple[0].append(selected_group_tuple[1](
            **selected_group_tuple[3])())

    except ValueError:
        print("Invalid option!")
        recursive_run()


if __name__ == "__main__":
    recursive_run()
