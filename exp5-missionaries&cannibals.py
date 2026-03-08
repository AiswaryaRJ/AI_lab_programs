import heapq

def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if (m > 0 and m < c) or (3 - m > 0 and 3 - m < 3 - c):
        return False
    return True

def a_star_missionaries():
    start = (3, 3, 1)  # m_left, c_left, boat_left
    goal = (0, 0, 0)
    queue = []
    heapq.heappush(queue, (0, start, []))  # cost, state, path
    visited = set()
    visited.add(start)
    while queue:
        cost, (m, c, b), path = heapq.heappop(queue)
        if (m, c, b) == goal:
            return path
        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
        for dm, dc in moves:
            if b == 1:  # boat left
                nm, nc = m - dm, c - dc
                nb = 0
            else:
                nm, nc = m + dm, c + dc
                nb = 1
            if is_valid(nm, nc) and is_valid(3 - nm, 3 - nc):
                new_state = (nm, nc, nb)
                if new_state not in visited:
                    visited.add(new_state)
                    h = nm + nc  # heuristic
                    heapq.heappush(queue, (cost + 1 + h, new_state, path + [(dm, dc, b)]))
    return None

def main():
    print("Missionaries and Cannibals Problem - A* Algorithm")
    print("Initial: 3 missionaries, 3 cannibals on left")
    print("Goal: All on right side\n")
    
    path = a_star_missionaries()
    if path:
        print(f"Solution found in {len(path)} moves:")
        for i, move in enumerate(path, 1):
            print(f"{i}. Missionaries: {move[0]}, Cannibals: {move[1]}, Boat: {'Left to Right' if move[2] == 1 else 'Right to Left'}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
