
# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates use of data classes along with constructors, attributes
# and properties in an object-oriented programming
# Change Log: (Who, When, What)
#   Monisha Grover,11/24/2024,Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Constants
MENU = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
-----------------------------------------
"""
FILE_NAME = "Enrollments.json"

# Variables
menu_choice = ""
students = []


class FileProcessor:
    """Handles file processing tasks."""

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        Reads data from a JSON file into a list of Student objects.
        param: file_name (name of the JSON file)
        return: student_data (list of dictionaries containing data from the json file)
        """
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                for entry in data:
                    student = Student(entry["first_name"], entry["last_name"], entry["course_name"])
                    student_data.append(student)
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
        except Exception as e:
            IO.output_error_messages("An unexpected error occurred while reading the file.", e)

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        Writes a list of Student objects to a JSON file.
        param: file_name (name of the JSON file)
        return: student_data (list of student objects to the json file)
        """
        try:
            with open(file_name, "w") as file:
                data = [student.to_dict() for student in student_data]
                json.dump(data, file)
            print(f"Data saved to '{file_name}'.")
        except Exception as e:
            IO.output_error_messages("An unexpected error occurred while writing to the file.", e)


class IO:
    """Handles input and output tasks."""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Displays error messages."""
        print(f"ERROR: {message}")
        if error:
            print(f"Details: {error}")

    @staticmethod
    def output_menu(menu: str):
        """Displays the menu."""
        print(menu)

    @staticmethod
    def output_student_courses(student_data: list):
        """Displays all registered student courses."""
        if not student_data:
            print("No registrations found.")
        else:
            for student in student_data:
                print(f"{student.first_name} {student.last_name} - {student.course_name}")

    @staticmethod
    def input_menu_choice():
        """Gets the user's menu choice."""
        try:
            return input("Enter your choice (1-4): ").strip()
        except Exception as e:
            IO.output_error_messages("An unexpected error occurred while getting menu choice.", e)

    @staticmethod
    def input_student_data(student_data: list):
        """Gets student registration data from the user."""
        try:
            first_name = input("Enter the student's first name: ").strip()
            if not first_name:
                raise ValueError("First name cannot be empty.")
            last_name = input("Enter the student's last name: ").strip()
            if not last_name:
                raise ValueError("Last name cannot be empty.")
            course_name = input("Enter the course name: ").strip()
            if not course_name:
                raise ValueError("Course name cannot be empty.")
            student = Student(first_name, last_name, course_name)
            student_data.append(student)
        except ValueError as e:
            IO.output_error_messages("Invalid input.", e)
        except Exception as e:
            IO.output_error_messages("An unexpected error occurred while getting student data.", e)


class Person:
    """Base class for a person."""

    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not value:
            raise ValueError("First name cannot be empty.")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not value:
            raise ValueError("Last name cannot be empty.")
        self._last_name = value


class Student(Person):
    """Class representing a student."""

    def __init__(self, first_name: str = "", last_name: str = "", course_name: str = ""):
        super().__init__(first_name, last_name)
        self.course_name = course_name

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        if not value:
            raise ValueError("Course name cannot be empty.")
        self._course_name = value

    def to_dict(self):
        """Converts the student data to a dictionary."""
        return {"first_name": self.first_name, "last_name": self.last_name, "course_name": self.course_name}


# Main Program Logic
if __name__ == "__main__":
    FileProcessor.read_data_from_file(FILE_NAME, students)
    while True:
        IO.output_menu(MENU)
        menu_choice = IO.input_menu_choice()
        if menu_choice == "1":
            IO.input_student_data(students)
        elif menu_choice == "2":
            IO.output_student_courses(students)
        elif menu_choice == "3":
            FileProcessor.write_data_to_file(FILE_NAME, students)
        elif menu_choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-4).")











            