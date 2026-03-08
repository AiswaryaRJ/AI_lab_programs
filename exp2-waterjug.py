"""
Water Jug Problem Solver

This program solves the classic water jug problem using Depth-First Search (DFS).
The problem involves two jugs of different capacities and a target amount of water to measure.

The jugs can be filled, emptied, or poured into each other. The goal is to find a sequence
of operations to reach the target amount in one of the jugs.

This implementation uses DFS to explore possible states and find a solution path.
"""

from collections import deque

def dfs_water_jug(cap4, cap3, goal):
    """
    Solves the water jug problem using DFS.

    Args:
    cap4 (int): Capacity of the 4-liter jug.
    cap3 (int): Capacity of the 3-liter jug.
    goal (int): Target amount of water to measure.

    Returns:
    list or None: List of states representing the solution path, or None if no solution.
    """
    stack = [(0, 0, [])]  # (jug4, jug3, path)
    visited = set()
    visited.add((0, 0))

    while stack:
        jug4, jug3, path = stack.pop()

        # Check if goal is reached
        if jug4 == goal or jug3 == goal:
            return path + [(jug4, jug3)]

        # Generate possible moves
        possible_moves = []

        # Fill 4-liter jug
        if jug4 < cap4:
            possible_moves.append((cap4, jug3))

        # Fill 3-liter jug
        if jug3 < cap3:
            possible_moves.append((jug4, cap3))

        # Empty 4-liter jug
        if jug4 > 0:
            possible_moves.append((0, jug3))

        # Empty 3-liter jug
        if jug3 > 0:
            possible_moves.append((jug4, 0))

        # Pour from 4 to 3
        if jug4 > 0 and jug3 < cap3:
            pour = min(jug4, cap3 - jug3)
            possible_moves.append((jug4 - pour, jug3 + pour))

        # Pour from 3 to 4
        if jug3 > 0 and jug4 < cap4:
            pour = min(jug3, cap4 - jug4)
            possible_moves.append((jug4 + pour, jug3 - pour))

        # Add unvisited states to stack
        for new_state in possible_moves:
            if new_state not in visited:
                visited.add(new_state)
                stack.append((new_state[0], new_state[1], path + [(jug4, jug3)]))

    return None

def main():
    cap4 = 4
    cap3 = 3
    goal = 2

    path = dfs_water_jug(cap4, cap3, goal)

    if path:
        print(f"Water Jug Problem: {cap4}L and {cap3}L jugs, goal {goal}L")
        print(f"Solution found with {len(path)} states:")
        for i, state in enumerate(path, 1):
            print(f"{i}. {state}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
