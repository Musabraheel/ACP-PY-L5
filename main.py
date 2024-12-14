def check_exam_eligibility(age, marks):
    """
    Check exam eligibility based on age and marks.

    :param age: int - Age of the student.
    :param marks: int - Marks scored by the student.
    :return: str - Eligibility message.
    """
    if age < 18:
        return "Not eligible: Minimum age is 18."
    elif marks < 40:
        return "Not eligible: Minimum passing marks are 40."
    else:
        return "Congratulations! You are eligible for the exam."

# Input from the user
try:
    user_age = int(input("Enter your age: "))
    user_marks = int(input("Enter your marks: "))
    result = check_exam_eligibility(user_age, user_marks)
    print(result)
except ValueError:
    print("Invalid input! Please enter valid integers for age and marks.")