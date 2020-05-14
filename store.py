"""
python3 store.py
The Dugout
 1. Running
 2. Baseball
 3. Basketball
 4. Exit
Select the number of a department
Attributes:
    - name
    - Departments
Optional Extra Attributes:
   - Store hours
   - Store capacity
"""
# Design patterns: How to program with OOP
# Composition: a "Has a" relationship
# Aggregation: a "Has a" relationship
# Polymorphism: Works on different data structures
from departments import Department
from products import Clothing, Swords


class Store:  # Dependant on the Dependant Class
    def __init__(self, name, departments=[]):
        self.name = name
        self.departments = departments
        # for dept in departments:
        #     department = Department(dept) # Composition. A type of a "has-a"
        #     self.departments.append(department)

    def __str__(self):
        output = ""
        output += self.name + "\n"
        for index, department in enumerate(self.departments):
            output += str(index + 1) + ". " + str(department.name) + "\n"
        output += str(len(self.departments) + 1) + ". Exit"
        return output

    def __repr__(self):
        return self


# Aggregation
running_products = [Clothing("shorts", 45, "Black"),
                    Clothing("sweat band", 12, "L", "Red")]
fencing_products = [Swords("epee", 75, 10), Swords("Saber", 75, 4)]
dugout_departments = [Department["Running"],
                      Department["Baseball"],
                      Department["Basketball"],
                      Department["Fencing"]]
store = Store("The Dugout", dugout_departments)
print(store)
selection = 0
while selection != len(store.departments) + 1:
    selection = input("Select the number of a department. ")
    try:
        selection = int(selection)
        if 1 <= selection < len(store.departments) + 1:
            print(f"the user selected: {selection}.")
            print(store.departments[selection - 1])
        elif selection == len(store.departments) + 1:
            print("Thank you for shopping with us today! :-)")
        else:
            print("Choose from the given choices")
    except ValueError:
        print("Choose a number, not an empty string or a letter or something")
    # A dynamic error message like, "please choose a number between 1 and 4"
