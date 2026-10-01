class Student:
    def __init__(self, first_name, last_name, num_courses):
        self.first_name = first_name
        self.last_name = last_name
        self.num_courses = num_courses

def fullTime(student):
   if (student.num_courses >= 3):
    return True
   else:
    return False

example_list = [
    Student("James", "Wilson", 4),
    Student("Olivia", "Martinez", 2),
    Student("Liam", "Johnson", 3),
    Student("Emma", "Brown", 1),
    Student("Noah", "Davis", 5),
    Student("Ava", "Garcia", 2),
    Student("Ethan", "Miller", 3),
    Student("Sophia", "Anderson", 0),
    Student("Mason", "Taylor", 4)
]

for s in example_list:
    if fullTime(s):
        print(s.first_name,s.last_name,"Full-time")
    else:
        print(s.first_name,s.last_name,"Part-time")