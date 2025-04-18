# Import the course data from a separate file
import course_data


def calculate_student_grade(data, student_name):
    # Check if student is in the roster
    if student_name not in data["roster"]:
        print("Student not found.")
        return
    #Set them to 0 by default
    total_weighted_score = 0
    total_weight = 0

    # Iterate through assignments and print the student's score
    # Or print 0 if there's no submission
    for assignment_name, assignment_info in data["assignments"].items():
        weight = assignment_info["weight"]
        submissions = assignment_info["submissions"]
        score = submissions.get(student_name, 0)  # Default to 0 if no submission

        # Print the assignment and score
        print(f"{assignment_name}: {score}%")

        # Calculate weighted score
        total_weighted_score += score * (weight / 100)
        total_weight += weight

    # Print the total grade (save to 1 decimal)
    final_grade = total_weighted_score
    print(f"Total grade: {final_grade:.1f}%")


# Ask the user for a student's name
student_name = input("Enter the student's name: ")
calculate_student_grade(course_data.actual_data, student_name)
