
import csv

def save_to_csv(data_list, file_name):
    if not file_name.lower().endswith(".csv"):
        print(f"Error: '{file_name}' must have a .csv extension.")
        return False
    
    if not data_list:
        print("Error: No student data to save.")
        return False

    is_saving = True
    while is_saving:
        try:
            with open(file_name, 'w', newline='', encoding='utf-8') as file:
                headers = ["id", "name", "age", "course", "status"]
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(data_list)
                print(f"Data successfully saved to {file_name}.")
                is_saving = False
        except IOError:
            print("Critical Error: Could not write to file.")
            is_saving = False

def load_from_csv(file_name):
    loaded_data = []
    error_count = 0
    skip_all_errors = False # Boolean flag to remember user decision
    
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                try:
                    # Manual type conversion and validation[span_2](end_span)
                    student_id = int(row["id"])
                    age = int(row["age"])
                    
                    if age <= 0:
                        raise ValueError("Age must be positive.")
                        
                    loaded_data.append({
                        "id": student_id,
                        "name": row["name"],
                        "age": age,
                        "course": row["course"],
                        "status": row["status"]
                    })
                except (ValueError, KeyError) as e:
                    error_count += 1
                    if not skip_all_errors:
                        print(f"\n[!] Data error: {e}")
                        print("1. Skip | 2. Skip all | 3. Cancel")
                        choice = input("Select: ")
                        if choice == "2":
                            skip_all_errors = True
                        elif choice == "3":
                            return None, error_count
            return loaded_data, error_count
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None, 0

                
        