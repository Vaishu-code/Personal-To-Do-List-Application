import json
import os

FILE_NAME = "tasks.json"

# ---------------- Task Class ----------------
class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def mark_completed(self):
        self.completed = True


# ---------------- File Handling ----------------
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return [Task(**task) for task in data]
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump([task.__dict__ for task in tasks], file, indent=4)


# ---------------- Task Operations ----------------
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter description: ")
    category = input("Enter category (Work/Personal/Urgent): ")

    tasks.append(Task(title, description, category))
    print("✅ Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task.completed else "Pending"
        print(f"\n{i}. {task.title}")
        print(f"   Description: {task.description}")
        print(f"   Category: {task.category}")
        print(f"   Status: {status}")


def mark_task_completed(tasks):
    view_tasks(tasks)
    index = int(input("Enter task number to mark completed: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index].mark_completed()
        print("✅ Task marked as completed.")
    else:
        print("❌ Invalid task number.")


def delete_task(tasks):
    view_tasks(tasks)
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("🗑️ Task deleted successfully.")
    else:
        print("❌ Invalid task number.")


# ---------------- Main Menu ----------------
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("💾 Tasks saved. Exiting...")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
