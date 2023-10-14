from collections import deque

def is_valid(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0

def lee_algorithm(grid, start, target):
    # Check if start and target are valid
    if not is_valid(*start, grid) or not is_valid(*target, grid):
        return None

    # Possible moves (up, down, left, right)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # Initialize the queue for BFS
    queue = deque()
    queue.append(start)

    # Initialize distance matrix with -1 (unvisited)
    distance = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    distance[start[0]][start[1]] = 0

    # Perform BFS
    while queue:
        x, y = queue.popleft()

        # Check if the target is reached
        if (x, y) == target:
            break

        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]

            if is_valid(new_x, new_y, grid) and distance[new_x][new_y] == -1:
                distance[new_x][new_y] = distance[x][y] + 1
                queue.append((new_x, new_y))

    # Reconstruct the path
    if distance[target[0]][target[1]] == -1:
        return None

    x, y = target
    path = [(x, y)]

    while (x, y) != start:
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if is_valid(new_x, new_y, grid) and distance[new_x][new_y] == distance[x][y] - 1:
                path.append((new_x, new_y))
                x, y = new_x, new_y
                break

    return path[::-1]  # Reverse the path to start from 'start'

# Example usage:
grid = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0]
]

start_point = (0, 0)
target_point = (4, 5)

path = lee_algorithm(grid, start_point, target_point)
if path:
    print("Shortest Path:")
    for step in path:
        print(step)
else:
    print("No path found.")
