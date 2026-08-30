# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

## Implementation Summary

I created list operations to insert, delete, and search through items using a real-world inventory scenario. I inserted inventory items at the beginning, middle, and end of a Python list. When an item was inserted, the elements following that index shifted to accommodate the new item.

I implemented deletion using `pop()` and validated the index before deleting so that an invalid index returned `None` instead of causing the program to crash. I also deleted items from the beginning, middle, and end of the list.

I implemented searching using a linear search that checked each element sequentially until it found the requested inventory item. When the item was found, its index was returned. When the item was not found, the search returned `-1`.

## Real-World Application

I used an inventory system as the real-world scenario for this assignment. A list can be used to store products or equipment in inventory. New items can be added, existing items can be removed, and the list can be searched to determine whether a particular item is in stock.