from utils import logger
from file_handler import initialize_file, write_record, read_records, overwrite_records
from record_manager import Record

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
            print(r.strip())
            return
    print("Record not found!\n")

@logger
def delete_record():
    del_id = input("Enter ID to delete: ")
    records = read_records()
    updated_records = []
    found = False

    for r in records:
        if r.startswith(del_id + ","):
            found = True
            continue
        updated_records.append(r.strip().split(","))

    if found:
        overwrite_records(updated_records)
        print(f"Record with ID {del_id} deleted successfully!\n")
    else:
        print("Record not found!\n")

@logger
def update_record():
    upd_id = input("Enter ID to update: ")
    records = read_records()
    updated_records = []
    found = False

    for r in records:
        fields = r.strip().split(",")
        if fields[0] == upd_id:
            found = True
            print("Enter new details (leave blank to keep current):")
            name = input(f"Name [{fields[1]}]: ") or fields[1]
            age = input(f"Age [{fields[2]}]: ") or fields[2]
            course = input(f"Course [{fields[3]}]: ") or fields[3]
            updated_records.append([upd_id, name, age, course, fields[4]])
        else:
            updated_records.append(fields)

    if found:
        overwrite_records(updated_records)
        print(f"Record with ID {upd_id} updated successfully!\n")
    else:
        print("Record not found!\n")

@logger
def main_menu():
    initialize_file()

    while True:
        print("\n--- Smart File & Data Management System ---")
        print("1. Add Record")
        print("2. View Records")
        print("3. Search Record")
        print("4. Delete Record")
        print("5. Update Record")
        print("6. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            search_record()
        elif choice == "4":
            delete_record()
        elif choice == "5":
            update_record()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main_menu()
