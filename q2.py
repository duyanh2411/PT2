import csv

class Employee:
    def __init__(self, code, name, salary, allowance):
        self.code = code
        self.name = name
        self.salary = salary
        self.allowance = allowance

def add_employee(code, name, salary, allowance):
    with open('input.txt', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([code, name, salary, allowance])
    print("Employee added successfully.")

def binary_search(employees, target_name):
    left = 0
    right = len(employees) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if employees[mid].name == target_name:
            return employees[mid]
        elif employees[mid].name < target_name:
            left = mid + 1
        else:
            right = mid - 1
    return None

def remove_employee(code):
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    with open('input.txt', 'w') as file:
        for line in lines:
            if not line.startswith(code + ','):
                file.write(line)
    print("Employee removed successfully.")

def print_sorted_employees():
    with open('input.txt', 'r') as file:
        reader = csv.reader(file)
        employees = [Employee(row[0], row[1], float(row[2]), float(row[3])) for row in reader]
    sorted_employees = sorted(employees, key=lambda x: x.salary + x.allowance, reverse=True)
    with open('result.txt', 'w') as file:
        writer = csv.writer(file)
        for employee in sorted_employees:
            writer.writerow([employee.code, employee.name, employee.salary, employee.allowance])
    print("Employees printed and saved in result.txt")

def main():
    while True:
        print("\n1. Add new employee")
        print("2. Find employee by name")
        print("3. Remove employee")
        print("4. Print employees in descending order of salary + allowance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            code = input("Enter employee code: ")
            name = input("Enter employee name: ")
            salary = float(input("Enter employee salary: "))
            allowance = float(input("Enter employee allowance: "))
            add_employee(code, name, salary, allowance)

        elif choice == '2':
            target_name = input("Enter employee name to search: ")
            with open('input.txt', 'r') as file:
                reader = csv.reader(file)
                employees = [Employee(row[0], row[1], float(row[2]), float(row[3])) for row in reader]
            result = binary_search(employees, target_name)
            if result:
                print("Employee found - Code:", result.code, "Name:", result.name, "Salary:", result.salary, "Allowance:", result.allowance)
            else:
                print("Employee not found.")

        elif choice == '3':
            code = input("Enter employee code to remove: ")
            remove_employee(code)

        elif choice == '4':
            print_sorted_employees()

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please enter again.")

if __name__ == "__main__":
    main()
