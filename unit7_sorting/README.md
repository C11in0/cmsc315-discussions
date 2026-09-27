# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare and constrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.

### My Reflection

In this assignment, I learned how Bubble Sort and Merge Sort can produce the same result while using very different approaches. I implemented Bubble Sort by comparing adjacent values and swapping them when they were out of order. I also implemented Merge Sort using recursion to divide a list into smaller sections and then merge them back together in sorted order. Working with Merge Sort helped me better understand the divide-and-conquer approach.

The biggest challenge for me was understanding the recursive process in Merge Sort. At first, it was difficult to visualize how repeatedly dividing the list eventually resulted in a sorted list. Testing the algorithm with smaller datasets helped me understand how the base case stopped the recursion and how the merge function rebuilt the list.

Bubble Sort was easier to understand and implement, but its O(n²) time complexity made it less efficient as the dataset increased. Merge Sort had O(n log n) time complexity, making it better for larger datasets, although it required additional memory. For small datasets, Bubble Sort could be acceptable, while Merge Sort would be a better choice for larger datasets.