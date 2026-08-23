# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

## Implementation Summary

I implemented a stack using a Python list and a queue using collections.deque. The stack used append() to add values and pop() to remove the most recently added value, which demonstrated Last-In, First-Out behavior.

I implemented the queue using append() to add values to the back and popleft() to remove values from the front. This demonstrated First-In, First-Out behavior.

I also tested several edge cases. The stack returned None when pop() or peek() was called while empty. The queue returned None when dequeue() or front() was called while empty. I also tested single-item stack and queue structures and verified that each became empty after the only item was removed.

The demonstration used actions for the stack and customers waiting for service for the queue.