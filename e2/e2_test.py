import numpy as np

from e2_classes import Person, ask_for_details

# Generate test cases
if __name__ == '__main__':
    params = {
        "name": ask_for_details("name"),
        "age": ask_for_details("age"),
        "gender": ask_for_details("gender (M/F)"),
        "weight": ask_for_details("weight"),
        "height": ask_for_details("height")
    }

    all_params = Person(**params)

    without_weight_and_height = Person(
        params['name'],
        params['age'],
        params['gender']
    )

    without_weight_and_height.weight = np.random.randint(75, 90)
    without_weight_and_height.height = np.random.random() + np.random.random()

    with_no_args = Person()

    # Default values
    print(with_no_args.__str__())

    for param in params:
        print(f"{param}: {params[param]}")
        # with_no_args.__setattr__(param,
        #                          int(params[param]) if param != 'name' or param != 'gender' else params[param])

    for person in [all_params, without_weight_and_height, with_no_args]:
        print(person.__str__())
        print(f"IMC: {person.findIMC()}")
        print(f"Is old enough: {person.is_old_enough()}")
        print(f"IMC designation: {person.define_imc()}")
