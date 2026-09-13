# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Implementation Summary

I implemented a Binary Search Tree using a Node class and a BST class. Each node stored a value along with references to its left and right child nodes.

I implemented recursive insertion so that values smaller than the current node were placed in the left subtree and larger values were placed in the right subtree. Duplicate values were ignored.

I implemented recursive searching that compared the target value to the current node and continued searching only the appropriate subtree. This reduced the number of values that needed to be examined when the tree was reasonably balanced.

I also implemented an in-order traversal that visited the left subtree, current node, and right subtree. This produced the values in sorted order.

The program tested successful and unsuccessful searches and also demonstrated edge cases involving an empty tree and duplicate values.

### Real-World Application

A real-world application of a Binary Search Tree could be organizing employee records by employee ID. Each employee ID could be stored as a node in the tree. IDs smaller than the current node would be placed in the left subtree, while larger IDs would be placed in the right subtree. This organization could make searching for a specific employee more efficient than checking every employee record one at a time when the tree is reasonably balanced.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

