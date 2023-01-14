import os

cls = lambda: os.system("cls")

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
