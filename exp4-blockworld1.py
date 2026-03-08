import heapq
import copy

def is_clear(state, block):
    for stack in state:
        if stack and stack[-1] == block:
            return True
    return False 

def get_stack_index(state, block):
    for i, stack in enumerate(state):
        if block in stack:
            return i
    return -1

def move_block(state, block, to_stack):
    new_state = copy.deepcopy(state)
    from_stack = get_stack_index(new_state, block)
    if from_stack == -1 or not new_state[from_stack] or new_state[from_stack][-1] != block:
        return None
    new_state[from_stack].pop()
    if to_stack == -1:  # to table
        new_state.append([block])
    else:
        new_state[to_stack].append(block)
    # Remove empty stacks
    new_state = [s for s in new_state if s]
    return new_state

def heuristic1(state, goal):
    # Number of blocks not in correct position
    goal_flat = [b for s in goal for b in s]
    state_flat = [b for s in state for b in s]
    count = 0
    for i, b in enumerate(state_flat):
        if i < len(goal_flat) and b != goal_flat[i]:
            count += 1
    return count

def heuristic2(state, goal):
    # Sum of misplaced blocks in stacks
    count = 0
    for s_state, s_goal in zip(state, goal):
        for i, b in enumerate(s_state):
            if i < len(s_goal) and b != s_goal[i]:
                count += 1
    return count

def heuristic3(state, goal):
    # Total blocks out of place
    goal_positions = {}
    for i, s in enumerate(goal):
        for j, b in enumerate(s):
            goal_positions[b] = (i, j)
    count = 0
    for i, s in enumerate(state):
        for j, b in enumerate(s):
            if b in goal_positions:
                gi, gj = goal_positions[b]
                if gi != i or gj != j:
                    count += 1
    return count

def best_first_search(initial, goal, heuristic):
    queue = []
    heapq.heappush(queue, (heuristic(initial, goal), initial, []))
    visited = set()
    visited.add(tuple(tuple(s) for s in initial))
    while queue:
        _, state, path = heapq.heappop(queue)
        if state == goal:
            return path
        for i, stack in enumerate(state):
            if stack:
                block = stack[-1]
                # Move to table
                new_state = move_block(state, block, -1)
                if new_state:
                    state_tuple = tuple(tuple(s) for s in new_state)
                    if state_tuple not in visited:
                        visited.add(state_tuple)
                        heapq.heappush(queue, (heuristic(new_state, goal), new_state, path + [(block, 'table')]))
                # Move to other stacks
                for j, other_stack in enumerate(state):
                    if j != i and (not other_stack or is_clear(state, other_stack[-1])):
                        new_state = move_block(state, block, j)
                        if new_state:
                            state_tuple = tuple(tuple(s) for s in new_state)
                            if state_tuple not in visited:
                                visited.add(state_tuple)
                                heapq.heappush(queue, (heuristic(new_state, goal), new_state, path + [(block, other_stack[-1] if other_stack else 'table')]))
    return None

def main():
    initial = [['E', 'B', 'F', 'D', 'A', 'C']]
    goal = [['A', 'D', 'B', 'E', 'F', 'C']]
    heuristics = [heuristic1, heuristic2, heuristic3]
    names = ["Heuristic 1: Misplaced blocks", "Heuristic 2: Stack mismatch", "Heuristic 3: Positional distance"]
    
    for h, name in zip(heuristics, names):
        print(f"{name}:")
        path = best_first_search(initial, goal, h)
        if path:
            print(f"  Moves: {len(path)}")
            for move in path:
                print(f"    {move}")
        else:
            print("  No solution")
        print()

if __name__ == "__main__":
    main()
