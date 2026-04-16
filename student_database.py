
# ---------------------- Student Database Class ----------------------

class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)


# ---------------------- Student  Class ----------------------

class Student:
    def __init__(self, student_id, name, department, is_enrolled=False):

        # Private attributes 
        self.__student_id = student_id 
        self.__name = name 
        self.__department = department 
        self.__is_enrolled = is_enrolled 

        StudentDatabase.add_student(self)

    def get_student_id(self):
        return self.__student_id

    def enroll_student(self):
        if self.__is_enrolled:
            print(f"Student {self.__name} is already enrolled.")
        else:
            self.__is_enrolled = True
            print(f"Student {self.__name} has been enrolled successfully.")

    def drop_student(self):
        if not self.__is_enrolled:
            print(f"Student {self.__name} is not currently enrolled.")
        else:
            self.__is_enrolled = False
            print(f"Student {self.__name} has been dropped successfully.")

    def view_student_info(self):
        status = "Enrolled" if self.__is_enrolled else "Not Enrolled"
        print(f"Student ID   : {self.__student_id}")
        print(f"Name         : {self.__name}")
        print(f"Department   : {self.__department}")
        print(f"Status       : {status}")
        print("-" * 30)


# Manually creating student objects
s1 = Student(101, "Sajid Ahmed", "CSE", True)
s2 = Student(102, "Nusrat Jahan", "EEE", True)
s3 = Student(103, "Tanvir Hasan", "BBA", False)


def find_student_by_id(student_id):
    for student in StudentDatabase.student_list:
        if student.get_student_id() == student_id:
            return student
    return None


while True:
    print("\n===== Student Management System =====")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(StudentDatabase.student_list) == 0:
            print("No students found.")
        else:
            for student in StudentDatabase.student_list:
                student.view_student_info()

    elif choice == "2":
        try:
            student_id = int(input("Enter student ID to enroll: "))
            student = find_student_by_id(student_id)

            if student is None:
                print("Error: Invalid student ID.")
            else:
                student.enroll_student()
        except ValueError:
            print("Error: Please enter a valid numeric student ID.")

    elif choice == "3":
        try:
            student_id = int(input("Enter student ID to drop: "))
            student = find_student_by_id(student_id)

            if student is None:
                print("Error: Invalid student ID.")
            else:
                student.drop_student()
        except ValueError:
            print("Error: Please enter a valid numeric student ID.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")