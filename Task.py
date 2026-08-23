def add_task(data):
    task = input("Task: ").strip()

    if not task:
        print("Task cannot be empty.")
        return

    data["tasks"][task] = {
        "complete": False
    }

    print("Task added.")


def view_tasks(data):
    if not data["tasks"]:
        print("No tasks yet.")
    else:
        for task, info in data["tasks"].items():
            status = "Completed" if info["complete"] else "Not completed"
            print(f"{task}: {status}")


def remove_task(data):
    task = input("Enter task to remove: ").strip()

    if task in data["tasks"]:
        del data["tasks"][task]
        print("Task removed.")
    else:
        print("Task not found.")


def mark_completed(data):
    task = input("Enter completed task: ").strip()

    if task in data["tasks"]:
        data["tasks"][task]["complete"] = True
        print("Task completed.")
    else:
        print("Task not found.")
