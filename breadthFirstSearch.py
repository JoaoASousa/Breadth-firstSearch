from queue import Queue



def create_maze():
    maze = []
    maze.append(['.', '.', '.', 'o', '.'])
    maze.append(['.', ' ', ' ', ' ', '.'])
    maze.append(['.', ' ', '.', '.', '.'])
    maze.append(['.', ' ', ' ', ' ', '.'])
    maze.append(['.', 'X', '.', '.', '.'])

    return maze

def start_end(maze):

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (maze[i][j] == 'o'):
                start_coords = [i,j]
            elif (maze[i][j] == 'X'):
                end_coords = [i,j]
    
    return (start_coords, end_coords)

def check_end(current, coords):
    pos = coords[0] # start position
    for c in current:
        if (c == 'U'): pos[1] += 1
        elif (c == 'D'): pos[1] -= 1
        elif (c == 'R'): pos[0] += 1
        elif (c == 'L'): pos[0] -= 1
    
    return (pos == coords[1])

def is_valid(elem_to_test, maze):
    return True


# function complete ?
def solve_maze(maze):

    coords = start_end(maze)
    start = coords[0]
    end = coords[1]

    print('Start: {}'.format(start))
    print('End  : {}'.format(end))

    q = Queue(0)
    q.put("")

    while True:
        current = q.get()

        if (check_end(current, coords)):
            print(current)
            break

        # U -> Up   D -> Down   L -> Left   R -> Right
        for i in ['U', 'D', 'L', 'R']:
            new_elem = current + i
            print(new_elem)
            if (is_valid(new_elem, maze)):
                q.put(new_elem)


def show_sol(maze, sol):
    pass




# if __name__ == "__main__":
#     maze = create_maze()
#     solve_maze(maze)

print(check_end('RUUU', [[2,1], [3,4]]))



# 0 0 0
# 0 0 0 0 0
# 0 1 0 0 0
# 0 0 0 0 1