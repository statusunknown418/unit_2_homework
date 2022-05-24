import pandas

from __helpers import (employee_options, professor_options, quit_program,
                       student_options)
from Employee import Employee
from Professor import Professor
from Student import Student

regular_employees = []

professors = []

students = []


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
