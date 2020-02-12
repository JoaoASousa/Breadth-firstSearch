from queue import Queue
from copy import deepcopy


def create_maze():
    maze = []
    maze.append(['.', '.', '.', 'o', '.'])
    maze.append(['.', ' ', ' ', ' ', '.'])
    maze.append(['.', ' ', '.', '.', '.'])
    maze.append(['.', ' ', ' ', ' ', '.'])
    maze.append(['.', 'x', '.', '.', '.'])

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
        print(maze[pos[0]][pos[1]])
        return False
    
    if (maze[pos[0]][pos[1]] == 'o'):
        maze[pos[0]][pos[1]] = 'O'
    
    print("VALID")
    return True

        

def solve_maze(maze):
    coords = find_start_end(maze)
    start = coords[0]
    end = coords[1]

    print('Start: {}'.format(start))
    print('End  : {}'.format(end))

    q = Queue(0)
    q.put("")

    while True:
        current = q.get()

        if (maze[coords[1][0]][coords[1][1]] == 'X'):
            print(current)
            break

        # U -> Up   D -> Down   L -> Left   R -> Right
        for i in ['U', 'D', 'L', 'R']:
            new_elem = current + i
            print(new_elem)
            if (check_move(maze, new_elem, coords)):
                q.put(new_elem)


def show_sol(maze, sol, coords):
    pass




if __name__ == "__main__":
    maze = create_maze()
    solve_maze(maze)

#print(check_end('RUUU', [[2,1], [3,4]]))



# 0 0 0
# 0 0 0 0 0
# 0 1 0 0 0
# 0 0 0 0 1