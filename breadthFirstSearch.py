from queue import Queue
from copy import deepcopy
import subprocess

import mazes


# from PIL import Image
# import numpy

# img = Image.open("m2.png")
# imgarr = numpy.array(img)

# for i in range(1000):
#     print(imgarr[i])


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
    
    if (pos[0] < 0 or pos[0] >= len(maze[0]) or pos[1] < 0 or pos[1] >= len(maze)):
        return False

    if (len(current) >= 2):
        # Doesn't make sense going in one direction and then going back right after
        if (current[-2:] == 'UD' or current[-2:] == 'DU' or current[-2:] == 'RL' or current[-2:] == 'LR'):
            return False

    if (pos == coords[1]):
        maze[coords[1][0]][coords[1][1]] = 'X' # X -> Found end with current path; x -> end not yet found
    
    elif (maze[pos[0]][pos[1]] != ' ' and maze[pos[0]][pos[1]] != 'o'):
        return False
    
    if (maze[pos[0]][pos[1]] == 'o'):
        maze[pos[0]][pos[1]] = 'O'
    
    return True


def solve_maze(maze, coords):
    elements_tested = 0
    q = Queue(0)
    q.put("")

    while True:
        current = q.get()

        # U -> Up   D -> Down   L -> Left   R -> Right
        for i in ['U', 'D', 'L', 'R']:
            new_elem = current + i
            # print(new_elem)
            elements_tested += 1
            if (check_move(maze, new_elem, coords)):
                q.put(new_elem)

                if (maze[coords[1][0]][coords[1][1]] == 'X'):
                    print('\nElements Tested: {}'.format(elements_tested))
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
    
    maze = mazes.create_maze_1()
    coords = find_start_end(maze)
    
    show_maze(maze)
    input("Press Any Key To Show The Solution")

    solution = solve_maze(maze, coords)
    show_sol(maze, solution, coords)