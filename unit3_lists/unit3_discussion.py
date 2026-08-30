"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Python's insert() method places the value at the requested index.

    # Existing elements at that index and after it are shifted one position

    # to the right to make room for the new value.

    lst.insert(index, value)

    # Inserting near the beginning or middle may require many elements to shift,

    # so it can take O(n) time. Inserting at the end generally requires less work.


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Validate the index before attempting deletion.

    # This prevents an IndexError and allows the program to handle invalid

    # operations safely instead of crashing.

    if index < 0 or index >= len(lst):

        return None

    # pop() removes the value at the specified index and returns it.

    # Elements after the removed value shift left to fill the empty position.

    return lst.pop(index)
def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This is a linear search because each element is checked sequentially

    # from the beginning of the list until the target value is found.

    for index in range(len(lst)):

        if lst[index] == value:

            return index

    # If every element has been checked and no match was found,

    # return -1 to indicate that the value is not in the list.

    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    # Create a starting list that represents inventory item names.

    inventory = ["Laptop", "Monitor", "Keyboard", "Mouse"]

    print("Original list:", inventory)

    # Insert an item at the beginning of the list.

    insert_at(inventory, 0, "Printer")

    print("After beginning insertion:", inventory)

    # Insert an item near the middle of the list.

    middle_index = len(inventory) // 2

    insert_at(inventory, middle_index, "Webcam")

    print("After middle insertion:", inventory)

    # Insert an item at the end of the list.

    insert_at(inventory, len(inventory), "Headset")

    print("After end insertion:", inventory)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    # Remove the first item in the list.

    removed = delete_at(inventory, 0)

    print("Removed from beginning:", removed)

    print("Updated list:", inventory)

    # Remove an item from the middle of the list.

    middle_index = len(inventory) // 2

    removed = delete_at(inventory, middle_index)

    print("Removed from middle:", removed)

    print("Updated list:", inventory)

    # Remove the final item in the list.

    removed = delete_at(inventory, len(inventory) - 1)

    print("Removed from end:", removed)

    print("Updated list:", inventory)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")


    # Search for an item that currently exists in the inventory.

    existing_value = "Monitor"

    result = search_value(inventory, existing_value)

    print(f"Search for '{existing_value}': found at index {result}")

    # Search for an item that is not currently stored in the inventory.

    missing_value = "Tablet"

    result = search_value(inventory, missing_value)

    print(f"Search for '{missing_value}': returned {result} because it was not found")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    # Edge case 1: Attempt to delete an index that does not exist.

    invalid_result = delete_at(inventory, 100)

    print("Delete using invalid index:", invalid_result)

    # Edge case 2: Insert a value into an empty list.

    empty_list = []

    insert_at(empty_list, 0, "First Item")

    print("Insert into empty list:", empty_list)

    # Edge case 3: Attempt to delete from an empty list.

    empty_delete = delete_at([], 0)

    print("Delete from empty list:", empty_delete)



if __name__ == "__main__":
    main()