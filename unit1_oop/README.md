# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.


## How the Program Works

This program demonstrates object-oriented programming by using a parent class to define common attributes and methods for an item. A child class inherits the functionality of the parent class and adds additional attributes and methods. This allows the program to reuse existing code while extending the functionality for more specific types of items.

The program also demonstrates Python namespaces by comparing class and instance namespaces. Shallow and deep copying are demonstrated to show how copied objects behave when they contain mutable data.

## Real-World Application

A real-world example of this structure would be an inventory management system. A general item class could store information such as an item's name and quantity, while specialized child classes could add information such as storage location and condition. Additional methods, such as checking whether an item is low on stock, could help identify when inventory needs to be replenished.