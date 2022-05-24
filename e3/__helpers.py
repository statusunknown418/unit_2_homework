import pandas


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
