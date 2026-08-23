import json
students = {}
def students_data():
    name = input("What is your name: ").strip()
    if name == "":
        print("Please enter your name.")
        return
    try:
        age = int(input("How old are you: ")) I 
        grade = int(input("What grade are you in: "))
        students[name] = {"age":age,"grade": grade}
        print(students)
    except ValueError:
         print("Invalid input please enter numbers only.")

def load_students():
    with open("student_data.json","r") as file:
        global students
        try:
            students = json.load(file)
        except FileNotFoundError:
            students = {}
def view_students():
    for name,info in students.items():
        print(f'Name: {name}')
        print(f'Age: {info["age"]}')
        print(f'Grade {info["grade"]}')
def saved_students():
    with open("student_data.json","w") as file:
        json.dump(students,file)
load_students()    
students_data()
view_students()
saved_students()
      
