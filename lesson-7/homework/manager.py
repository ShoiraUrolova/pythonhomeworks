import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, 'w'):
                pass

    def add_employee(self):
        employee_id = input("Enter Employee ID: ").strip()
        if self._is_duplicate_id(employee_id):
            print("Employee ID already exists. Please use a unique ID.")
            return

        name = input("Enter Name: ").strip()
        position = input("Enter Position: ").strip()
        salary = input("Enter Salary: ").strip()

        employee = Employee(employee_id, name, position, salary)
        with open(self.FILE_NAME, 'a') as file:
            file.write(str(employee) + '\n')
        print("Employee added successfully!")

    def view_all_employees(self):
        with open(self.FILE_NAME, 'r') as file:
            records = file.readlines()
            if records:
                print("Employee Records:")
                for record in records:
                    print(record.strip())
            else:
                print("No employee records found.")

    def search_employee(self):
        employee_id = input("Enter Employee ID to search: ").strip()
        found = False
        with open(self.FILE_NAME, 'r') as file:
            for line in file:
                if line.startswith(employee_id + ','):
                    print("Employee Found:")
                    print(line.strip())
                    found = True
                    break
        if not found:
            print("Employee not found.")

    def update_employee(self):
        employee_id = input("Enter Employee ID to update: ").strip()
        records = []
        updated = False
        with open(self.FILE_NAME, 'r') as file:
            records = file.readlines()

        with open(self.FILE_NAME, 'w') as file:
            for line in records:
                if line.startswith(employee_id + ','):
                    print("Employee Found:")
                    print(line.strip())
                    name = input("Enter new Name (leave blank to keep current): ").strip()
                    position = input("Enter new Position (leave blank to keep current): ").strip()
                    salary = input("Enter new Salary (leave blank to keep current): ").strip()

                    details = line.strip().split(', ')
                    name = name if name else details[1]
                    position = position if position else details[2]
                    salary = salary if salary else details[3]

                    updated_employee = Employee(employee_id, name, position, salary)
                    file.write(str(updated_employee) + '\n')
                    updated = True
                else:
                    file.write(line)

        if updated:
            print("Employee information updated successfully!")
        else:
            print("Employee not found.")

    def delete_employee(self):
        employee_id = input("Enter Employee ID to delete: ").strip()
        records = []
        deleted = False
        with open(self.FILE_NAME, 'r') as file:
            records = file.readlines()

        with open(self.FILE_NAME, 'w') as file:
            for line in records:
                if line.startswith(employee_id + ','):
                    deleted = True
                else:
                    file.write(line)

        if deleted:
            print("Employee record deleted successfully!")
        else:
            print("Employee not found.")

    def _is_duplicate_id(self, employee_id):
        with open(self.FILE_NAME, 'r') as file:
            for line in file:
                if line.startswith(employee_id + ','):
                    return True
        return False

    def menu(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.view_all_employees()
            elif choice == '3':
                self.search_employee()
            elif choice == '4':
                self.update_employee()
            elif choice == '5':
                self.delete_employee()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()