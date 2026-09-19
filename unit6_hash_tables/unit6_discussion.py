"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")

    # Create an empty dictionary that will act as our hash table.
    student_records = {}

    # Each student ID is a unique key that maps to a student's name.
    # Python dictionaries behave like hash tables by using a hash
    # function to determine where each key-value pair is stored.
    student_records["S1001"] = "James"
    student_records["S1002"] = "Maria"
    student_records["S1003"] = "David"
    student_records["S1004"] = "Ashley"
    student_records["S1005"] = "Michael"

    # Display the contents of the dictionary.
    print("Student records:", student_records)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # A dictionary allows us to retrieve a value by using its key.
    # Here, the student ID is used to locate the student's name.
    print("Looking up S1002:", student_records["S1002"])
    print("Looking up S1004:", student_records["S1004"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")

    print("Before update:", student_records)

    # Assigning a new value to an existing key replaces the old value.
    # The key remains the same, but the information associated with it changes.
    student_records["S1003"] = "Daniel"

    print("After update:", student_records)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")

    print("Before deletion:", student_records)

    # The del statement removes both the key and its associated value
    # from the dictionary.
    del student_records["S1005"]

    print("After deletion:", student_records)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Attempt to look up a student ID that does not exist.
    # Using get() prevents the program from crashing if the key is missing.
    missing_student = student_records.get("S9999")

    if missing_student is None:
        print("S9999 was not found in the student records.")
    else:
        print("S9999:", missing_student)

    # Edge Case 2: Safely attempt to delete a key that does not exist.
    # Checking for the key first prevents a KeyError.
    if "S2000" in student_records:
        del student_records["S2000"]
        print("S2000 was deleted.")
    else:
        print("S2000 cannot be deleted because it does not exist.")

    # Display the final contents of the hash table.
    print("\n=== FINAL STUDENT RECORDS ===")
    print(student_records)


if __name__ == "__main__":
    main()