## Description

This program is a modular python console application designed for a educational test.

## Features

- Student management: Create, read, update, and delete.

- Data fields: Each record includes a unique ID, name, age, course, and status(Active/Inactive).

- Data Persistence: Capacity to save and load information from .csv files to maintain data between sessions.

- Statics: view intitusional reports such as the total count of active students and the oldest student registred.

-input: validation users try/except block and logical loops to prevent the program from crashing due to invalid user input.

## Structure

1. main.py: The entry point containing the interactive menu.

2. student_services: Contains the core logic and data procesing functions.

3. manager: Hadles CSV reading and writing operations.

## Requirements
- Python 3.x

## How to use
1. opne your terminal or command prompt
2. navigate to the project folder.
3. run the application using the following command: python3 main.py

## Example of use

1. select option 1 from the mnu
2. enter a unique ID
3. provide the student's Name, Age and Course
4. System will automatically set the status to Active
