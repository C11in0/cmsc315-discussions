"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    category = "General Equipment"

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def display_info(self):
        return f"Item: {self.name}, Quantity: {self.quantity}, Category: {self.category}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    item_type = "Training Equipment"

    def __init__(self, name, quantity, location, condition):
        super().__init__(name, quantity)
        self.location = location
        self.condition = condition

    def display_location(self):
        return f"{self.name} is located at {self.location}"

    def check_stock(self):
        if self.quantity < 10:
            return f"{self.name} is low on stock."
        else:
            return f"{self.name} has sufficient stock."

    def display_info(self):
        return (f"Item: {self.name}, Quantity: {self.quantity}, "
                f"Category: {self.category}, Type: {self.item_type}, "
                f"Location: {self.location}, Condition: {self.condition}")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    item1 = ChildClass("Water Can", 10, "Warehouse A", "Serviceable")
    item2 = ChildClass("Tent", 5, "Warehouse B", "Serviceable")

    # Access the class variable through the class itself.
    print("Class variable through class:", ChildClass.item_type)

    # Access the same class variable through an object.
    print("Class variable through object:", item1.item_type)

    # Add an attribute to only item1.
    item1.serial_number = "WC001"

    # Display each object's instance namespace.
    print("Item 1 namespace:", item1.__dict__)
    print("Item 2 namespace:", item2.__dict__)

    # Display information from the class namespace.
    print("Child class namespace:", ChildClass.__dict__)



# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = {
        "item": "Water Can",
        "locations": ["Warehouse A", "Training Area"]
    }

    shallow = copy(original)
    deep = deepcopy(original)

    # Modify the nested list in the original object.
    original["locations"].append("Supply Room")

    # A shallow copy shares nested objects with the original,
    # so the new location will also appear in shallow.
    print("Original:", original)
    print("Shallow copy:", shallow)

    # A deep copy creates an independent copy of nested objects,
    # so the new location will not appear in deep.
    print("Deep copy:", deep)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Create and test a parent object.
    print("\n=== Parent Object ===")
    parent_item = ParentClass("Water Can", 10)
    print(parent_item.display_info())

    # Create and test a child object.
    print("\n=== Child Object ===")
    child_item = ChildClass("Tent", 5, "Warehouse B", "Serviceable")
    print(child_item.display_info())
    print(child_item.display_location())
    print(child_item.check_stock())
    # Test an edge case with zero inventory.
    print("\n=== Edge Case: Zero Inventory ===")
    empty_item = ChildClass("Sleeping Bag", 0, "Warehouse A", "Serviceable")
    print(empty_item.display_info())
    print(empty_item.check_stock())

    # Demonstrate namespaces and copying.
    demonstrate_namespaces()
    demonstrate_copying()



if __name__ == "__main__":
    main()