"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """

        # In a BST, smaller values belong on the left side
        # and larger values belong on the right side.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """

        # If an empty position is reached, create a new node.
        if node is None:
            return Node(value)

        # Smaller values are recursively inserted into
        # the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values are recursively inserted into
        # the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # If the value is equal to the current node's value,
        # no new node is created. This prevents duplicates.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """

        # A BST can reduce the search space after each comparison.
        # Instead of checking every value like a linear search,
        # the BST chooses either the left or right subtree.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        # Reaching an empty position means the value
        # does not exist in the tree.
        if node is None:
            return False

        # The value was found at the current node.
        if value == node.value:
            return True

        # A smaller value can only be located in
        # the left subtree.
        if value < node.value:
            return self._search_recursive(node.left, value)

        # A larger value can only be located in
        # the right subtree.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """

        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        if node is not None:
            # First visit the left subtree, which contains
            # values smaller than the current node.
            self._inorder_recursive(node.left, values)

            # Visit the current node.
            values.append(node.value)

            # Finally visit the right subtree, which contains
            # values larger than the current node.
            self._inorder_recursive(node.right, values)

            # Because BST values are organized as
            # left < current < right, visiting nodes in this
            # order produces the values in sorted order.


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    # Create an empty BST.
    tree = BST()

    # These values create nodes on both the left and right
    # sides of the root.
    values = [50, 30, 70, 20, 40, 60, 80]

    # Insert each value into the BST.
    for value in values:
        tree.insert(value)

    print("Values inserted:", values)

    # A BST reduces the search space because each comparison
    # determines whether to continue searching left or right.
    # When the tree is reasonably balanced, this avoids
    # examining every value in the tree.

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    # In-order traversal visits the left subtree first,
    # followed by the current node and then the right subtree.
    # Since a BST stores smaller values on the left and larger
    # values on the right, the result is sorted.
    traversal = tree.inorder()
    print("In-order traversal:", traversal)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # 40 and 70 were inserted into the tree,
    # so both searches should return True.
    print("Search for 40:", tree.search(40))
    print("Search for 70:", tree.search(70))

    # 25 and 90 were not inserted into the tree,
    # so both searches should return False.
    print("Search for 25:", tree.search(25))
    print("Search for 90:", tree.search(90))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # Edge Case 1:
    # An empty tree has no root. Searching it should return
    # False, while traversing it should return an empty list.
    empty_tree = BST()

    print("Search empty tree for 10:", empty_tree.search(10))
    print("Traverse empty tree:", empty_tree.inorder())

    # Edge Case 2:
    # This BST ignores duplicate values because the recursive
    # insertion method only inserts values that are smaller
    # or larger than an existing node.
    tree.insert(50)

    print("After attempting to insert duplicate 50:", tree.inorder())


if __name__ == "__main__":
    main()