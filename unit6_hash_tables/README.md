# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment used Python dictionaries to demonstrate hash table behavior. I created a student record system where student IDs were used as keys and student names were stored as values.

## Learning Objectives

- Inserted key-value pairs
- Retrieved values efficiently
- Updated existing values
- Removed entries
- Demonstrated edge cases
- Applied hashing concepts to a real-world scenario

## Implementation

I created an empty Python dictionary called `student_records` and added five student records. Each student ID served as a unique key, while the student's name served as the associated value.

I demonstrated lookup operations by searching for two existing student IDs and displaying their names. I also updated an existing student's name to demonstrate how assigning a new value to an existing key replaces the previous value.

For the delete operation, I removed one student record from the dictionary and displayed the dictionary before and after the deletion.

## Edge Cases

I tested two edge cases. First, I attempted to look up a student ID that did not exist. I used the `get()` method so the program could handle the missing key without causing an error.

Second, I attempted to delete a student ID that did not exist. I checked whether the key existed before deleting it, which prevented a `KeyError`.

## Hash Table Behavior

Python dictionaries behave like hash tables by using a hash function to determine where keys and their associated values are stored. This allows values to be retrieved efficiently by their keys.

A collision can occur when different keys produce the same hash table location. Python handles collisions internally so that the correct value can still be retrieved. Hash tables improve efficiency because searching for a key is typically much faster than searching through every item one at a time.

## Real-World Scenario

The program represented a student record lookup system. Student IDs were used as unique keys, making it possible to quickly retrieve, update, or remove a student's information.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150-200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.