import yaml
from os import system, path
import readline


# utility function to clear the screen
cls = lambda: system("cls")

# function to prefill input for editing tasks/actions
def input_with_prefill(prompt, text) -> str:
    text = str(text)

    def hook():
        readline.insert_text(text)
        readline.redisplay()

    readline.set_pre_input_hook(hook)
    result = input(prompt)
    readline.set_pre_input_hook()
    return result


# Prompt user to validate their playbook name choice
def validate_playbook_name(choices) -> bool:
    print(f"Playbook Name: {choices}")
    valid: str = input("Does Everything look good? (y/n)\n> ")
    if valid not in ["y", "n"]:
        return validate_playbook_name(choices)
    if valid == "y":
        return True
    return False


# prompt user for playbook name
def get_playbook_name() -> str:
    playbook_name: str = input("Enter the name of the playbook:\n> ")
    cls()
    if not validate_playbook_name(playbook_name):
        return get_playbook_name()
    return playbook_name


# clean data for empty strings and have user validate
def validate_hosts(hosts: list[str]) -> list | None:
    verified: list = []
    for host in hosts:
        host = host.strip()
        # empty string filter
        if host and host.strip():
            verified.append(host)
    print("Hosts: " + str(verified))
    valid: str = input("Does everything look okay? (y/n)\n> ")
    if valid not in ["y", "n"]:
        return validate_hosts(hosts)
    if valid == "y":
        return verified
    return None


# prompt user for hosts
def get_hosts() -> list:
    cls()
    hosts: list = input(
        "\nEnter the hosts for the playbook (comma separated):\n> "
    ).split(",")
    cls()
    valid_hosts = validate_hosts(hosts)
    if not valid_hosts:
        return get_hosts()
    return valid_hosts


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


def print_tasks(tasks) -> list[str]:
    indexes: list[str] = []
    for i in range(0, len(tasks)):
        indexes.append(i)
        print(f"{i + 1}) {tasks[i]}")
    return indexes


def print_vars(vars: dict) -> list[str]:
    indexes: list[str] = []
    i = 0
    for key, value in vars.items():
        indexes.append(key)
        print(f"{i + 1}) {key} : {value}")
        i += 1
    return indexes


# validate the tasks
def validate_tasks(tasks: list) -> list:
    cls()
    print_tasks(tasks)
    valid: str = input(
        "------\nDoes everything look okay? (Enter 'e' to edit an entry) (y/n)\n> "
    )
    if valid not in ["y", "n", "e"]:
        return validate_tasks(tasks)
    if valid == "y":
        return tasks
    if valid == "n":
        return get_tasks()
    if valid == "e":
        index: int = -1
        while index not in range(0, len(tasks)):
            cls()
            for i, task in enumerate(tasks):
                print(f"{i + 1}) {task}")
            index: int = (
                int(input(f"\n------\nWhich entry to edit? (1-{len(tasks)})\n> ")) - 1
            )
        tasks[index] = update_task(tasks[index])
    return validate_tasks(tasks)


def validate_vars(vars: list) -> list:
    print(vars)
    cls()
    indexes = print_vars(vars)
    valid: str = input(
        "------\nDoes everything look okay? (Enter 'e' to edit an entry) (y/n)\n> "
    )
    if valid not in ["y", "n", "e"]:
        return validate_tasks(vars)
    if valid == "y":
        return vars
    if valid == "n":
        return get_tasks()
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
    return validate_tasks(vars)


def update_task(task: dict) -> dict:
    cls()
    print("{")
    for key, value in task.items():
        print(f"{key} : {value}")
    print("}")
    index: str = input(
        f"------\nWhich variable to edit? enter ('n' for name or 'a' action)\n> "
    )
    if index in ["n", "a"]:
        if index == "n":
            index = "name"
        if index == "a":
            index = "action"
        new_item = input_with_prefill(
            "\npress Enter when done editing to save\n> ", task[index]
        )
        task[index] = new_item
        return task
    return update_task(task)


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
    return update_task(var)


# prompt user for tasks and actions
def get_tasks(type: str = None) -> list[dict]:
    task_count = lambda: print(f"Actions: [{len(tasks)}]")
    next_t = lambda: " next" if tasks else ""
    cls()
    tasks: list = []
    while True:
        cls()
        task_count()
        task_name: str = input(
            f"Enter the NAME of the{next_t()} task (or 'q' to quit):\n> "
        ).strip()
        if task_name == "q":
            break
        cls()
        task_count()
        task: dict = {"name": task_name}
        task["action"] = input(f"Enter the ACTION for '{task_name}':\n> ").strip()
        tasks.append(task)
    if not validate_tasks(tasks):
        return get_tasks()
    return tasks


def new_playbook(output_dir: str | None = None) -> None:
    cls()
    playbook = {}

    playbook_name = "butts"

    # # Prompt for the playbook name
    playbook_name = get_playbook_name()
    playbook["name"] = playbook_name

    # Prompt for the hosts
    cls()
    print("PLAYBOOK: " + playbook_name)
    playbook["hosts"] = get_hosts()

    # Prompt for the tasks
    cls()
    print("PLAYBOOK: " + playbook_name)
    # print("Hosts: " + playbook["hosts"])
    playbook["tasks"] = get_tasks()

    playbook["vars"] = get_vars()
    # Write the playbook to a file
    if output_dir != None and path.exists(output_dir):
        file_name = path.join(output_dir, playbook_name)
    else:
        file_name = playbook_name
    with open(f"{file_name}.yml", "w") as f:
        yaml.dump(playbook, f)

    print("Playbook created successfully!")


# new_playbook()
# update_var({"variable": "a value", "variable": "a value"})
get_vars()
