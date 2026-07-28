# This is Day 17 project : Student Report Generator

import csv

def process_student_data(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            reader = csv.DictReader(infile)
            student_reports = []
            
            for row in reader:
                name = row['Name']
                math = int(row['Math'])
                science = int(row['Science'])
                english = int(row['English'])
                
                marks = [math, science, english]
                
                if not all(0 <= mark <= 100 for mark in marks):
                    raise ValueError("Marks must be between 0 and 100.")
                
                average = round((math + science + english) / 3, 2)
                status = "Pass" if average >=60 else "Fail"
                grade = "A" if average >= 90 else "B" if average >= 80 else "C" if average >= 70 else "D" if average >=60 else "F"
                
                student_reports.append({
                    'Name' : name,
                    'Math' : math,
                    'Science' : science,
                    'English' : english,
                    'Average' : average,
                    'Status' : status,
                    'Grade' : grade
                })
            
            if not student_reports:
                print("No student records found.")
                return
            
            highest_average = max(student['Average'] for student in student_reports)

            for student in student_reports:
                if student['Average'] == highest_average:
                    student['Top Performer'] = "Yes"
                else:
                    student['Top Performer'] = "No"
                
        with open(output_file, 'w', newline='') as outfile:
            fieldnames = ['Name', 'Math', 'Science', 'English', 'Average', 'Status', 'Grade', 'Top Performer']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(student_reports)
            
        search_student(student_reports)
            
        print(f"\nStudent report generated successfully : '{output_file}'")
    
    except FileNotFoundError:
        print(f"Error : File '{input_file}' not found")
    except KeyError:
        print("Error : Invalid column names in the input file")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred : {e}")
        
def search_student(student_reports):
    search_name = input("\nEnter the student name to search: ").strip().lower()

    if not search_name:
        print("Student name cannot be empty.")
        return

    found = False

    for student in student_reports:
        if search_name in student['Name'].lower():
            print("\n------ Student Details ------\n")
            print(f"Name: {student['Name']}")
            print(f"Math: {student['Math']}")
            print(f"Science: {student['Science']}")
            print(f"English: {student['English']}")
            print(f"Average: {student['Average']:.2f}")
            print(f"Grade: {student['Grade']}")
            print(f"Status: {student['Status']}")
            print(f"Top Performer: {student['Top Performer']}")
            print("-" * 40)

            found = True

    if not found:
        print("Student not found.")
        
input_file = 'students.csv'
output_file = 'student_report.csv'

process_student_data(input_file, output_file)

# Done