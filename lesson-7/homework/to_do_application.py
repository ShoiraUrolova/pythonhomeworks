import json
import csv
from datetime import datetime
from abc import ABC, abstractmethod
from json.tool import main

# Task class
class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

    def to_dict(self):
        return self.__dict__

# TaskManager class
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for task in self.tasks:
                print(task)

    def update_task(self, task_id, **kwargs):
        for task in self.tasks:
            if task.task_id == task_id:
                for key, value in kwargs.items():
                    setattr(task, key, value)
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self, status):
        filtered = [task for task in self.tasks if task.status == status]
        if filtered:
            print("Filtered Tasks:")
            for task in filtered:
                print(task)
        else:
            print("No tasks found with the given status.")

# Abstract base class for file handlers
class FileHandler(ABC):
    @abstractmethod
    def save(self, tasks, filename):
        pass

    @abstractmethod
    def load(self, filename):
        pass

# CSVHandler class
class CSVHandler(FileHandler):
    def save(self, tasks, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=tasks[0].to_dict().keys())
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())
        print("Tasks saved to CSV.")

    def load(self, filename):
        tasks = []
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(Task(**row))
        print("Tasks loaded from CSV.")
        return tasks

# JSONHandler class
class JSONHandler(FileHandler):
    def save(self, tasks, filename):
        with open(filename, mode='w') as file:
            json.dump([task.to_dict() for task in tasks], file)
        print("Tasks saved to JSON.")

    def load(self, filename):
        tasks = []
        with open(filename, mode='r') as file:
            data = json.load(file)
            for item in data:
                tasks.append(Task(**item))
        print("Tasks loaded from JSON.")
        return tasks

# Main application
if __name__ == "__main__":
    manager = TaskManager()
    handlers = {"csv": CSVHandler(), "json": JSONHandler()}
    current_handler = handlers["json"]

    while True:
        print("""
        1. Add a new task
        2. View all tasks
        3. Update a task
        4. Delete a task
        5. Filter tasks by status
        6. Save tasks
        7. Load tasks
        8. Exit
        """)
        choice = input("Enter your choice: ")

        if choice == "1":
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ") or None
            status = input("Enter Status (Pending/In Progress/Completed): ")
            manager.add_task(Task(task_id, title, description, due_date, status))

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            task_id = input("Enter Task ID to update: ")
            updates = {}
            if input("Update Title? (y/n): ") == "y":
                updates["title"] = input("Enter new Title: ")
            if input("Update Description? (y/n): ") == "y":
                updates["description"] = input("Enter new Description: ")
            if input("Update Due Date? (y/n): ") == "y":
                updates["due_date"] = input("Enter new Due Date (YYYY-MM-DD): ")
            if input("Update Status? (y/n): ") == "y":
                updates["status"] = input("Enter new Status: ")
            manager.update_task(task_id, **updates)

        elif choice == "4":
            task_id = input("Enter Task ID to delete: ")
            manager.delete_task(task_id)

        elif choice == "5":
            status = input("Enter status to filter by: ")
            manager.filter_tasks(status)

        elif choice == "6":
            filename = input("Enter filename to save: ")
            current_handler.save(manager.tasks, filename)

        elif choice == "7":
            filename = input("Enter filename to load: ")
            manager.tasks = current_handler.load(filename)

        elif choice == "8":
            print("Exiting application.")
            break

        else:
            print("Invalid choice. Please try again.")
          
if __name__=="__main__":
    main()