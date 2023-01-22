import yaml
from os import system, path
from pb_name import get_playbook_name
from utils import input_with_prefill
from pb_hosts import get_hosts
from pb_tasks import get_tasks
from pb_vars import get_vars

# utility function to clear the screen
cls = lambda: system("cls")


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


if __name__ == "__main__":
    ...
    # new_playbook()
    # update_var({"variable": "a value", "variable": "a value"})
    get_vars()
