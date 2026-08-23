"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return None
        #pop() removes the most recently added value, following LIFO behavior.
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            return None
        # peek() returns the top value without removing it from the stack.
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return None
        # popleft() removes the oldest value, following FIFO behavior.
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty():
            return None
        #front() returns the oldest value without removing it from the queue.
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


    print("\n=== STACK DEMO ===")

    # Create a stack and add four values.
    stack = Stack()
    stack.push("Action 1")
    stack.push("Action 2")
    stack.push("Action 3")
    stack.push("Action 4")

    print("Four actions were added to the stack.")
    print("Current top of stack:", stack.peek())

    # Remove each value to demonstrate Last-In, First-Out behavior.
    print("\nRemoving items demonstrates LIFO behavior:")
    print("Removed:", stack.pop())
    print("Removed:", stack.pop())
    print("Removed:", stack.pop())
    print("Removed:", stack.pop())

    # Test popping and peeking when the stack is empty.
    print("\nTesting an empty stack:")
    print("Pop from empty stack:", stack.pop())
    print("Peek at empty stack:", stack.peek())

    # Test the single-item edge case.
    single_stack = Stack()
    single_stack.push("Only Item")
    print("\nSingle-item stack test:")
    print("Removed:", single_stack.pop())
    print("Is the stack empty?", single_stack.is_empty())

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")

    # Create a queue and add four customers.
    queue = Queue()
    queue.enqueue("Customer 1")
    queue.enqueue("Customer 2")
    queue.enqueue("Customer 3")
    queue.enqueue("Customer 4")

    print("Four customers were added to the queue.")
    print("Customer currently at the front:", queue.front())

    # Remove each customer to demonstrate First-In, First-Out behavior.
    print("\nServing customers demonstrates FIFO behavior:")
    print("Served:", queue.dequeue())
    print("Served:", queue.dequeue())
    print("Served:", queue.dequeue())
    print("Served:", queue.dequeue())

    # Test dequeuing and viewing the front when the queue is empty.
    print("\nTesting an empty queue:")
    print("Dequeue from empty queue:", queue.dequeue())
    print("Front of empty queue:", queue.front())

    # Test the single-item edge case.
    single_queue = Queue()
    single_queue.enqueue("Only Customer")
    print("\nSingle-item queue test:")
    print("Served:", single_queue.dequeue())
    print("Is the queue empty?", single_queue.is_empty())

if __name__ == "__main__":
    main()
