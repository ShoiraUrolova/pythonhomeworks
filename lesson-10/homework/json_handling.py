import json
import csv

# Load tasks from JSON file
def load_tasks(filename="tasks.json"):
    with open(filename, "r") as file:
        tasks = json.load(file)
    return tasks

# Save tasks back to JSON file
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

# Display all tasks
def display_tasks(tasks):
    print(f"{'ID':<5} {'Task Name':<20} {'Completed':<10} {'Priority':<8}")
    print("-" * 45)
    for task in tasks:
        print(f"{task['id']:<5} {task['task']:<20} {str(task['completed']):<10} {task['priority']:<8}")

# Calculate task statistics
def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks if total_tasks > 0 else 0

    print("\nTask Completion Stats:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority:.2f}")

# Convert tasks to CSV
def tasks_to_csv(tasks, filename="tasks.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        # Write the task data
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])

# Main program execution
def main():
    # Load tasks from JSON
    tasks = load_tasks()

    # Display tasks
    print("Task List:")
    display_tasks(tasks)

    # Display stats
    calculate_stats(tasks)

    # Modify a task (example: mark task with ID 1 as completed)
    for task in tasks:
        if task['id'] == 1:
            task['completed'] = True

    # Save changes back to JSON
    save_tasks(tasks)

    # Convert tasks to CSV
    tasks_to_csv(tasks)
    print("\nTasks saved to tasks.json and converted to tasks.csv.")

if __name__ == "__main__":
    main()