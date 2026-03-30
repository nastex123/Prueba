#Recuerda, debes terminar el manager.py

from student_services import *
from manager import *

def main_menu():
    students = []
    system_on = True

    while system_on:
        print("System")
        print("1. Register Student.")
        print("2. List all.")
        print("3. Search by ID.")
        print("4. Update Student.")
        print("5. Delete Student.")
        print("6. statistics.")
        print("7. Save to CSV.")
        print("8. Load from CSV.")
        print("9. Exit.")

        choice = input("Select (1-9)")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            if not students: print("List is empty.")
            else:
                for s in students:
                    print(f"{s['id']} | {s['name']} | {s['course']} | {s['status']}")
        elif choice == "3":
            s_id = validate_input("Search ID: ",int)
            res = find_student(students, s_id)
            if res: print(f"Found: {res["name"]} - {res["course"]} - ({res["status"]})")
            else: print("Not found.")
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            res = get_stats(students)
            if res: print(f"Archive: {res["active"]} / Oldest: {res["oldest"]}")
                
        elif choice == "7":
            path = input("Filename (e.g: students.csv): ")
            save_to_csv(students, path)
        elif choice == "8":
            path = input("Filename to load (e.g: students.csv): ")
            data, err = load_from_csv(path)
            if data is not None:
                print(f"Loaded with {err} errors.")
                deciding = True

                while deciding:
                    mode = input("(O)verwrite or (M)erge? ").upper()
                    if mode == "O": students = data; deciding = False
                    elif mode == "M":
                        for item in data:
                            if not find_student(students, item["id"]):
                                students.append(item)
                        deciding = False
        elif choice == "9":
            print("Goodbye!"); system_on =False

main_menu()