import os
from utils import input_with_prefill

cls = lambda: os.system("cls")


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


def print_tasks(tasks) -> list[str]:
    indexes: list[str] = []
    for i in range(0, len(tasks)):
        indexes.append(i)
        print(f"{i + 1}) {tasks[i]}")
    return indexes
