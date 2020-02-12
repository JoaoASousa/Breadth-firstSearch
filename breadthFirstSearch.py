from queue import Queue
from copy import deepcopy
import subprocess


def create_maze():
    maze = []
    
    maze.append(['.', '.', '.', 'o', '.'])
    maze.append(['.', ' ', ' ', ' ', '.'])
    maze.append(['.', ' ', '.', '.', '.'])
    maze.append(['.', ' ', ' ', ' ', '.'])
    maze.append(['.', 'x', '.', '.', '.'])

    return maze


def create_maze_2():
    maze = []

    maze.append(['.', '.', '.', '.', '.'])
    maze.append(['o', ' ', ' ', ' ', '.'])
    maze.append(['.', ' ', '.', ' ', '.'])
    maze.append(['.', ' ', ' ', ' ', '.'])
    maze.append(['.', '.', 'x', '.', '.'])

    return maze


def create_maze_3():
    maze = []
    
    maze.append(['.', '.', '.', 'o', '.', '.'])
    maze.append(['.', ' ', ' ', ' ', ' ', '.'])
    maze.append(['.', ' ', '.', '.', ' ', '.'])
    maze.append(['.', ' ', ' ', ' ', ' ', '.'])
    maze.append(['.', ' ', ' ', ' ', ' ', '.'])
    maze.append(['.', '.', '.', 'x', '.', '.'])

    return maze


def find_start_end(maze):

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (maze[i][j] == 'o'):
                start_coords = [i,j]
            elif (maze[i][j] == 'x'):
                end_coords = [i,j]
    
    return (start_coords, end_coords)


def check_move(maze, current, coords):
    pos = deepcopy(coords[0]) # start position
    for c in current:
        if (c == 'U'): pos[0] -= 1
        elif (c == 'D'): pos[0] += 1
        elif (c == 'R'): pos[1] += 1
        elif (c == 'L'): pos[1] -= 1
    
    if (pos[0] < 0 or pos[0] > len(maze[0]) or pos[1] < 0 or pos[1] > len(maze)):
        return False

    if (pos == coords[1]):
        maze[coords[1][0]][coords[1][1]] = 'X' # X -> Found end with current path; x -> end not yet found
    
    elif (maze[pos[0]][pos[1]] != ' ' and maze[pos[0]][pos[1]] != 'o'):
        return False
    
    if (maze[pos[0]][pos[1]] == 'o'):
        maze[pos[0]][pos[1]] = 'O'
    
    return True


def solve_maze(maze, coords):

    q = Queue(0)
    q.put("")

    while True:
        current = q.get()

        # U -> Up   D -> Down   L -> Left   R -> Right
        for i in ['U', 'D', 'L', 'R']:
            new_elem = current + i
            # print(new_elem)
            if (check_move(maze, new_elem, coords)):
                q.put(new_elem)

                if (maze[coords[1][0]][coords[1][1]] == 'X'):
                    print('\nSolution:')
                    print(new_elem)
                    return new_elem


def show_sol(maze, solution, coords):
    pos = deepcopy(coords[0])

    for c in solution:
        if (c == 'U'): pos[0] -= 1
        elif (c == 'D'): pos[0] += 1
        elif (c == 'R'): pos[1] += 1
        elif (c == 'L'): pos[1] -= 1

        if (maze[pos[0]][pos[1]] != 'X'):
            maze[pos[0]][pos[1]] = '+'
    
    for row in maze:
        print(row)


def show_maze(maze):

    for row in maze:
        print(row)


if __name__ == "__main__":

    subprocess.run('clear')
    print()
    maze = create_maze_3()
    coords = find_start_end(maze)
    
    show_maze(maze)
    input("Press Any Key To Show The Solution")

    solution = solve_maze(maze, coords)
    show_sol(maze, solution, coords)