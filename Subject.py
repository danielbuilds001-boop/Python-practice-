student = {}
def name():
    student_name = input("Enter your name: ").strip()
    if student_name == "":
        print("Your name cannot be empty.")
        return
    else:
        try:
            math = int(input("Enter your score for math: "))
            eng = int(input("Enter the score for English: "))

            student[student_name] = {"grades": {"maths":math,"English":eng}}
            print(student)
        except ValueError:
            print("Invalid input please try again.")
            return
    

name()
