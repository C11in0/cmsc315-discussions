"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # If the starting node is not in the graph,
    # return an empty list so the program does not crash.
    if start not in graph:
        return []

    # A queue is used because BFS visits nodes in the order
    # they are discovered, which allows it to move level by level.
    queue = deque([start])

    # The visited set prevents the same node from being processed
    # more than once.
    visited = {start}

    # This list stores the order in which nodes are visited.
    traversal_order = []

    # Continue until there are no more nodes left in the queue.
    while queue:

        # Remove the node at the front of the queue.
        current = queue.popleft()

        # Add the current node to the traversal result.
        traversal_order.append(current)

        # Check each neighbor connected to the current node.
        for neighbor in graph[current]:

            # Only add neighbors that have not already been visited.
            if neighbor not in visited:

                # Mark the neighbor as visited before adding it
                # to the queue so it is not added multiple times.
                visited.add(neighbor)

                # Neighbors are added to the end of the queue
                # so BFS processes them in discovery order.
                queue.append(neighbor)

    # BFS explores nearby nodes first, while depth-first search
    # follows one path as far as possible before backtracking.
    return traversal_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    # This graph represents buildings on a college campus.
    # Each key is a building, which represents a node.
    # Each value contains the buildings directly connected to it.
    # The connections represent walking paths between buildings.
    graph = {
        "Library": ["Science Hall", "Student Center"],
        "Science Hall": ["Library", "Engineering Hall", "Gym"],
        "Student Center": ["Library", "Cafeteria"],
        "Engineering Hall": ["Science Hall", "Cafeteria"],
        "Gym": ["Science Hall"],
        "Cafeteria": ["Student Center", "Engineering Hall"]
    }

    print("\n=== GRAPH STRUCTURE ===")

    # Display each building and its direct connections.
    for building, neighbors in graph.items():
        print(f"{building}: {neighbors}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")

    start_node = "Library"

    # BFS begins at the Library and then visits its direct neighbors.
    # After that, it visits nodes connected to those neighbors.
    traversal = bfs(graph, start_node)

    print(f"Starting node: {start_node}")
    print("BFS traversal order:", traversal)

    # Add a new building to demonstrate how the graph can change.
    graph["Dormitory"] = ["Gym"]

    # Because the graph represents walking paths, add the
    # connection from Gym back to Dormitory as well.
    graph["Gym"].append("Dormitory")

    print("\nAdded new building: Dormitory")
    print("Updated BFS traversal:", bfs(graph, start_node))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1:
    # Start from a node that does not exist.
    # The BFS function returns an empty list instead of crashing.
    print("\nEdge Case 1 - Missing start node:")
    print(bfs(graph, "Parking Garage"))

    # Edge Case 2:
    # A graph with only one node should simply return that node.
    single_node_graph = {
        "Library": []
    }

    print("\nEdge Case 2 - Single-node graph:")
    print(bfs(single_node_graph, "Library"))

    # Edge Case 3:
    # Starting from a different building changes the traversal order.
    print("\nEdge Case 3 - Different starting node:")
    print(bfs(graph, "Gym"))


if __name__ == "__main__":
    main()