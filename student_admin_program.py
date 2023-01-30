import csv

def add_student(file_name, name, student_id, courses, grades):
    """
    Add a new student to the database file
    """
    with open(file_name, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, student_id, courses, grades])

def get_student(file_name, student_id):
    """
    Get the details of a student with the given ID
    """
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == student_id:
                return row
    return None

def update_student(file_name, student_id, courses, grades):
    """
    Update the courses and grades of a student with the given ID
    """
    students = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == student_id:
                row[2] = courses
                row[3] = grades
            students.append(row)
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(students)

def delete_student(file_name, student_id):
    """
    Delete the student with the given ID from the database
    """
    students = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] != student_id:
                students.append(row)
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(students)

# Example usage:

# Add a new student
add_student("students.csv", "John Doe", "12345", "Math,Science,History", "A,B,C")

# Get the details of a student
student = get_student("students.csv", "12345")
print(student) # ['John Doe', '12345', 'Math,Science,History', 'A,B,C']

# Update the courses and grades of a student
update_student("students.csv", "12345", "Math,Science,English", "A,A,B")
student = get_student("students.csv", "12345")
print(student) # ['John Doe', '12345', 'Math,Science,English', 'A,A,B']

# Delete a student
delete_student("students.csv", "12345")
student = get_student("students.csv", "12345")
print(student) # None
