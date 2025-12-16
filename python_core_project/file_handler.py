import os

FILE_NAME = "records.csv"

def initialize_file():
    """Create CSV file if it doesn't exist"""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            f.write("ID,Name,Age,Course,Created_At\n")

def write_record(record):
    """Append a new record"""
    with open(FILE_NAME, "a") as f:
        f.write(",".join(record) + "\n")

def read_records():
    """Read all records"""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return f.readlines()[1:]  # skip header

def overwrite_records(records):
    """Overwrite CSV with updated records"""
    with open(FILE_NAME, "w") as f:
        f.write("ID,Name,Age,Course,Created_At\n")
        for record in records:
            f.write(",".join(record) + "\n")
