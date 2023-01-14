import os
from utils import input_with_prefill

cls = lambda: os.system("cls")


def get_vars() -> dict:
    variables = {}
    task_count = lambda: print(f"Actions: [{len(variables.items())}]")
    next_t = lambda: " next " if variables else " new "
    cls()
    task_count()
    while True:
        cls()
        task_count()
        variable_name = input(f"Enter{next_t}variable name press 'q' to quit.")
        if variable_name == "q":
            break
        cls()
        task_count()
        value = input(f"Enter a value for {variable_name}")
        variables[variable_name.strip()] = value.strip()
    if not validate_vars(variables):
        get_vars()
    return variables


def print_vars(vars: dict) -> list[str]:
    indexes: list[str] = []
    i = 0
    for key, value in vars.items():
        indexes.append(key)
        print(f"{i + 1}) {key} : {value}")
        i += 1
    return indexes


def validate_vars(vars: list) -> list:
    print(vars)
    cls()
    indexes = print_vars(vars)
    valid: str = input(
        "------\nDoes everything look okay? (Enter 'e' to edit an entry) (y/n)\n> "
    )
    if valid not in ["y", "n", "e"]:
        return validate_vars(vars)
    if valid == "y":
        return vars
    if valid == "n":
        return get_vars()
    if valid == "e":
        index: int = -1
        while index not in range(0, len(vars)):
            cls()
            i = 0
            for key, value in vars.items():
                print(f"{i + 1}) {key}: {value}")
                i += 1
            index: str = indexes[
                int(input(f"\n------\nWhich entry to edit? (1-{len(vars)})\n> ")) - 1
            ]

        vars[index] = update_var(vars[index])
    return validate_vars(vars)


def update_var(var: dict) -> dict:
    cls()
    print("{")
    key = None
    value = None
    for key, value in var.items():
        print(f"{key} : {value}")
    print("}")
    index: str = input(
        f"------\nWhich variable to edit? enter ('n' for name or 'v' value)\n> "
    )
    if index in ["n", "v"]:
        if index == "n":
            index = key
        if index == "a":
            index = value
        new_item = input_with_prefill(
            "\npress Enter when done editing to save\n> ", var[index]
        )
        var[index] = new_item
        return var
    return update_var(var)
