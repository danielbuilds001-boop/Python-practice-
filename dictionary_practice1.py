school = {
    "students": {
        "Daniel": {
            "math": 90,
            "science": 85
        },
        "Sarah": {
            "math": 95,
            "science": 88
        }
    }
}
print(school["students"]["Daniel"]["science"])
print(school["students"]["Sarah"]["math"])
school["students"]["Daniel"]["english"]= 92
school["students"]["Daniel"]["english"]= 90
average = school["students"]["Daniel"] = school["math + science + english"]

for name, grades in school["students"].items():
    highest = 0
    average = grades
    if grades > average:
        print(name, grades["math"])