import os

cls = lambda: os.system("cls")

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
