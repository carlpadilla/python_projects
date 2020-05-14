"""
python3 store.py
The Dugout
  1. Running
  2. Baseball
  3. Basketball
  4. Exit
Select the number of a department.

Attributes:
- name
- departments

Optional extra attributes:
- Store hours
- Store capacity
"""

# Composition: a "has-a" relationship
# Polymorphism: works on different data structures

from departments import Department


class Store:

    def __init__(self, name, departments):
        self.name = name
        self.departments = []

        for dep in departments:
            department = Department(dep)
            self.departments.append(department)

    def __str__(self):
        output = ""

        output += self.name + "\n"

        for index, department in enumerate(self.departments):
            output += str(index + 1) + ". " + str(department) + "\n"

        output += str(len(self.departments) + 1) + ". Exit"
        return output

    def __repr__(self):
        return self


store = Store("The Dugout", ["Running", "Baseball", "Basketball", "Fencing"])

print(store)

# Right now if we exit this prints "Choose from the given choices" and then the exit message
# We'll want to fix that too! good catch Stephanie

selection = 0
while selection != len(store.departments) + 1:
    selection = input("Select the number of a department. ")
    try:
        selection = int(selection)
        if selection >= 1 and selection < len(store.departments) + 1:
            print(f"the user selected: {selection}")
        else:
            print("Choose from the given choices")
    except ValueError:
        print("Choose a number, not an empty string or a letter or something")
    # a dynamic error message like, “please choose a number between 1 and 4”

print("Thank you for shopping with us today! :-) ")
