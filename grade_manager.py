
# Student Grade Manager
# Week 1 - Day 2 Assignment

# Store student details
students = []


# Calculate grade based on mark
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


# Add a new student
def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Error: Name cannot be empty.")
        return

    try:
        mark = int(input("Enter mark (0-100): "))

        if mark < 0 or mark > 100:
            print("Error: Mark must be between 0 and 100.")
            return

    except ValueError:
        print("Error: Please enter a valid whole number.")
        return

    student = {
        "name": name,
        "mark": mark
    }

    students.append(student)

    print("Student added successfully!")


# Display student results and statistics
def show_results():
    if not students:
        print("No students added yet.")
        return

    name_width = max(24, max(len(s["name"]) for s in students) + 2)
    line_width = name_width + 16

    print("\nSTUDENT RESULTS")
    print("-" * line_width)
    print(f"{'Name':<{name_width}}{'Mark':>8}{'Grade':>8}")
    print("-" * line_width)

    marks = []

    for student in students:
        name = student["name"]
        mark = student["mark"]
        grade = get_grade(mark)

        print(f"{name:<{name_width}}{mark:>8}{grade:>8}")

        marks.append(mark)

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print("-" * line_width)
    print(f"Average: {average:.1f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")


# Main menu
def main():
    while True:
        print("\n===== STUDENT GRADE MANAGER =====")
        print("1. Add Student")
        print("2. Show Results")
        print("3. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            show_results()

        elif choice == "3":
            print("Thank you! Goodbye.")
            break

        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


# Start the application
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram closed. Goodbye!")
