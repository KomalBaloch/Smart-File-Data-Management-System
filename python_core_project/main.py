# ===============================
# Smart File & Data Management System
# Core Python Project
# Author: Komal Sakhidad
# ===============================

"""
PROJECT OVERVIEW:
This is a menu-driven CLI based Python application that manages user records
using core Python concepts such as:
- Functions
- File Handling
- OOP (Classes)
- Error Handling
- Decorators
- Datetime

Files Included (logical separation):
1. main.py
2. record_manager.py
3. file_handler.py
4. utils.py

"""

# ===============================
# utils.py
# ===============================
from datetime import datetime

def logger(func):
    """Decorator for logging function calls"""
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} called at {datetime.now()}")
        return func(*args, **kwargs)
    return wrapper

# ===============================
# file_handler.py
# ===============================
FILE_NAME = "records.csv"

def initialize_file():
    try:
        with open(FILE_NAME, "x") as f:
            f.write("ID,Name,Age,Course,Created_At\n")
    except FileExistsError:
        pass


def write_record(record):
    with open(FILE_NAME, "a") as f:
        f.write(",".join(record) + "\n")


def read_records():
    with open(FILE_NAME, "r") as f:
        return f.readlines()[1:]

# ===============================
# record_manager.py
# ===============================
class Record:
    def __init__(self, record_id, name, age, course):
        self.record_id = record_id
        self.name = name
        self.age = age
        self.course = course
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_list(self):
        return [self.record_id, self.name, self.age, self.course, self.created_at]

# ===============================
# main.py
# ==============================
@logger
def add_record():
    try:
        record_id = input("Enter ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        record = Record(record_id, name, age, course)
        write_record(record.to_list())
        print("Record added successfully!\n")

    except Exception as e:
        print("Error:", e)


@logger
def view_records():
    records = read_records()
    if not records:
        print("No records found!\n")
        return

    for r in records:
        print(r.strip())
    print()


@logger
def search_record():
    search_id = input("Enter ID to search: ")
    records = read_records()

    for r in records:
        if r.startswith(search_id + ","):
            print("Record Found:")
            print(r)
            return

    print("Record not found!\n")


@logger
def main_menu():
    initialize_file()

    while True:
        print("\n--- Smart File & Data Management System ---")
        print("1. Add Record")
        print("2. View Records")
        print("3. Search Record")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            search_record()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main_menu()
