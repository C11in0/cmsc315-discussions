"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # Linear search checks each element one at a time from
    # the beginning of the list until the target is found.
    # In the worst case, every element must be checked.
    # Because the number of comparisons grows with the size
    # of the list, linear search has O(n) time complexity.
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    # If the entire list is searched and the target is
    # not found, return -1.
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    left = 0
    right = len(lst) - 1

    while left <= right:
        # Find the middle position of the remaining search area.
        middle = (left + right) // 2

        if lst[middle] == target:
            return middle

        # If the target is greater than the middle value,
        # eliminate the entire left half of the search area.
        elif lst[middle] < target:
            left = middle + 1

        # If the target is smaller than the middle value,
        # eliminate the entire right half of the search area.
        else:
            right = middle - 1

        # Each iteration removes approximately half of the
        # remaining values, giving binary search O(log n)
        # time complexity.

    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    small_data = [10, 20, 30, 40, 50, 60, 70]

    print("Small dataset:", small_data)

    # Test a value that exists in the dataset.
    existing_target = 50

    print(
        "Linear search for",
        existing_target,
        ":",
        linear_search(small_data, existing_target)
    )

    print(
        "Binary search for",
        existing_target,
        ":",
        binary_search(small_data, existing_target)
    )

    # Both searches return index 4 because the value 50
    # is located at index 4 in the list.

    # Test a value that does not exist in the dataset.
    missing_target = 55

    print(
        "Linear search for",
        missing_target,
        ":",
        linear_search(small_data, missing_target)
    )

    print(
        "Binary search for",
        missing_target,
        ":",
        binary_search(small_data, missing_target)
    )

    # Both searches return -1 because 55 is not in the list.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    large_data = list(range(1, 10001))
    large_target = 9999

    print("Large dataset contains 10,000 values.")

    print(
        "Linear search for",
        large_target,
        ":",
        linear_search(large_data, large_target)
    )

    print(
        "Binary search for",
        large_target,
        ":",
        binary_search(large_data, large_target)
    )

    # Both algorithms find 9999 at index 9998.
    #
    # Linear search may need to examine almost every value
    # before reaching the target. Binary search repeatedly
    # cuts the remaining search area in half. This becomes
    # significantly more efficient as the dataset grows.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list
    empty_list = []

    print(
        "Linear search on empty list:",
        linear_search(empty_list, 10)
    )

    print(
        "Binary search on empty list:",
        binary_search(empty_list, 10)
    )

    # Both searches return -1 because there are no values
    # available to search.

    # Edge Case 2: Single-element list
    single_item = [25]

    print(
        "Linear search on single-element list:",
        linear_search(single_item, 25)
    )

    print(
        "Binary search on single-element list:",
        binary_search(single_item, 25)
    )

    # Both searches return index 0 because 25 is the only
    # element in the list.

    # Edge Case 3: Value at the first position
    print(
        "Linear search for first value:",
        linear_search(small_data, 10)
    )

    print(
        "Binary search for first value:",
        binary_search(small_data, 10)
    )

    # Both searches correctly return index 0.

    # Edge Case 4: Value at the last position
    print(
        "Linear search for last value:",
        linear_search(small_data, 70)
    )

    print(
        "Binary search for last value:",
        binary_search(small_data, 70)
    )

    # Both searches correctly return index 6.


if __name__ == "__main__":
    main()