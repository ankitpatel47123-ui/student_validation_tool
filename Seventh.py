# Reliable Student Records Import & Validation Tool
import json
import os
class StudentValidationError(Exception):
    """Raised when student record is invalid"""
    pass
INPUT_FILE = "students_input.json"
VALID_FILE = "students_valid.json"
ERROR_FILE = "import_errors.txt"

if not os.path.exists(INPUT_FILE):
    sample = {
        "S101": {"name": "Aman", "marks": [78, 65, 88]},
        "S102": {"name": "Riya", "marks": [45, 150]},
        "S103": {"marks": [60, 70, 80]} 
    }
    with open(INPUT_FILE, 'w') as f:
        json.dump(sample, f, indent=2)

accepted = {}
errors = []

print(f"Import started: {INPUT_FILE}")

try:
    with open(INPUT_FILE, 'r') as f:
        data = json.load(f) 

except FileNotFoundError:
    print(f"Error: {INPUT_FILE} not found")
    exit()
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON format - {e}")
    exit()
else:
    print("File read successfully, validating records...")
finally:
    pass
count = 0
for sid, info in data.items():
    count += 1
    try:
        if 'name' not in info:
            raise KeyError("missing required field 'name'")
        
        if 'marks' not in info:
            raise KeyError("missing required field 'marks'")

        marks = info['marks']
        
        if not isinstance(marks, list) or len(marks) != 3:
            raise StudentValidationError("marks must contain exactly 3 values between 0 and 100.")
        
        for m in marks:
            if not (0 <= m <= 100):
                raise StudentValidationError("marks must contain exactly 3 values between 0 and 100.")

        accepted[sid] = info
        print(f"Accepted: {sid} - {info['name']}")

    except KeyError as e:
        msg = f"Rejected record {count}: {e}"
        print(msg)
        errors.append(msg)
    except StudentValidationError as e:
        msg = f"Rejected record {count}: {e}"
        print(msg)
        errors.append(msg)
    except Exception as e:
        msg = f"Rejected record {count}: Unexpected error - {e}"
        print(msg)
        errors.append(msg)
try:
    with open(VALID_FILE, 'w') as f:
        json.dump(accepted, f, indent=2)
    
    with open(ERROR_FILE, 'w') as ef:
        ef.write("\n".join(errors))

except IOError as e:
    print(f"Failed to write output files: {e}")

else:
    print(f"\nImport completed.")
    print(f"Accepted records: {len(accepted)}")
    print(f"Rejected records: {len(errors)}")
    print(f"Valid output: {VALID_FILE}")
    print(f"Error log: {ERROR_FILE}")