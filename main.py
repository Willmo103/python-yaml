import yaml
from os import system as sys, path

cls = lambda: sys("cls")


def validate_playbook_name(choices) -> bool:
    print(f"Playbook Name: {choices}")
    valid = input("Does Everything look good? (y/n)\n> ")
    if valid not in ["y", "n"]:
        return validate_playbook_name(choices)
    if valid == "y":
        return True
    return False


def get_playbook_name() -> str:
    playbook_name = input("Enter the name of the playbook:\n> ")
    cls()
    if not validate_playbook_name(playbook_name):
        return get_playbook_name()
    return playbook_name


def validate_hosts(hosts: list[str]) -> list | None:
    verified = []
    for host in hosts:
        host = host.strip()
        if host and host.strip():
            verified.append(host)
    print("Hosts: " + str(verified))
    valid = input("Does everything look okay? (y/n)\n> ")
    if valid not in ["y", "n"]:
        return validate_hosts(hosts)
    if valid == "y":
        return verified
    return None


def get_hosts() -> function | list:
    cls()
    hosts = input("\nEnter the hosts for the playbook (comma separated):\n> ").split(
        ","
    )
    cls()
    valid_hosts = validate_hosts(hosts)
    if valid_hosts == None:
        return get_hosts()
    return valid_hosts


def new_playbook(output_dir=None):
    cls()
    playbook = {}

    # # Prompt for the playbook name
    playbook_name = get_playbook_name()
    playbook["name"] = playbook_name

    # Prompt for the hosts
    cls()
    print("PLAYBOOK: " + playbook["name"])
    playbook["hosts"] = get_hosts()

    # Prompt for the tasks
    tasks = []
    while True:
        task_name = input("Enter the name of the task (or 'q' to quit):\n> ")
        if task_name == "q":
            break
        task = {"name": task_name}
        task["action"] = input("Enter the action for the task:\n> ")
        tasks.append(task)
    playbook["tasks"] = tasks

    # Write the playbook to a file
    if output_dir != None and path.exists(output_dir):
        file_name = path.join(output_dir, playbook_name)
    else:
        file_name = playbook_name
    with open(f"{file_name}.yml", "w") as f:
        yaml.dump(playbook, f)

    print("Playbook created successfully!")


new_playbook()
