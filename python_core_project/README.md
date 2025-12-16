# Smart File & Data Management System

A **Python-based command-line application** to manage records using CSV files. Designed to demonstrate **Python OOP, file handling, decorators, and modular programming**.

---

## Features

- Add a new record (ID, Name, Age, Course)  
- View all records in the CSV file  
- Search a record by ID  
- Delete a record by ID  
- Update an existing record  
- Automatic logging of function calls with timestamps  

---

## How It Works

1. Run `main.py` using Python 3.x  
2. The program displays a menu:
- Add Record
- View Records
- Search Record
- Delete Record
- Update Record
- Exit

3. Enter your choice and follow the prompts.  
4. All records are stored in `records.csv` automatically.

---

## Project Structure

python_core_project/
│
├─ main.py # Main menu and program logic
├─ utils.py # Logger decorator and file functions
├─ file_handler.py # Functions to read/write CSV file
├─ record_manager.py # Record class
└─ records.csv # CSV file storing all records

---

## How to Run

1. Make sure Python 3.x is installed.  
2. Open terminal/command prompt in the project folder:  


```bash
cd python_core_project```

3. Run the program:
python main.py

