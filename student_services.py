#TOdo el jodido codigo hay que traducirlo luego.

def validate_input(message, data_type):
    is_valid = True
    while is_valid:
        try:
            value = data_type(input(message))
            if value < 0:
                print("Error")
                continue
            return value
        except ValueError:
            print("Error")
            
def find_student(student_list, search_id):
   
    for s in student_list:
        if s["id"] == search_id:
            return s
        return None
    
def add_student(student_list):
    s_id = validate_input("id: ",int)
    
    if find_student(student_list, s_id):
        print(f"Error: ID {s_id} is already taken.")
        return
    
    name= input("Name ")
    age= validate_input("Age: ",int)
    course= input("Course: ")
    
    student_list.append({
        "id": s_id, "name": name, "age": age, 
        "course": course, "status": "Active"
    })
    print("Student added succesfully")

def delete_student(student_list):
    search_id = validate_input("Enter ID to delete: ",int)
    student = find_student(student_list, search_id)

    if student:
        confirm = input(f"Are u sure u want to delete{student["name"]}? (y/n)")
        if confirm.lower() == "y":
            student_list.remove(student)
            print("Student removed.")
    else:
        print("student no found.")
    
def update_student(student_list):
    search_id = validate_input("Enter ID to update: ", int)
    student = find_student(student_list, search_id)
    
    if not student:
        print("Student not found."); return

    is_editing = True
    while is_editing:
        print(f"\nEditing: {student['name']}")
        print("1. Name () 2. Age / 3. Course / 4. Status / 5. Back")
        opt = input("Choice: ")
        
        if opt == "1": student["name"] = input("New Name: ")
        elif opt == "2": student["age"] = validate_input("New Age: ", int)
        elif opt == "3": student["course"] = input("New Course: ")
        elif opt == "4":
            student["status"] = "Inactive" if student["status"] == "Active" else "Active"
            print(f"Status is now: {student['status']}")
        elif opt == "5": is_editing = False

        
def get_stats(student_list):
    if not student_list: 
        return None

    active = len([s for s in student_list if s ["status"] == "Active"])
    oldest = max(student_list, key = lambda x: x["age"])

    return {
       "active": active, "oldest": oldest
    }

