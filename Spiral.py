#File: Spiral.py

#Description: prints surrounding values of central value of spiral

#Student's Name: Jaeho Jang

#Student's UT EID: jj36386

#Course Name: CS 313E

#Unique Number: 50300

#Date Created: 2/17/20

#Date Last Modified: 2/17/20

#  Input: dim is a positive odd integer
#  Output: function returns a 2-D list of integers arranged
#          in a spiral
def create_spiral(dim):
    #starting indexs
    turning = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}
    x = dim // 2
    y = dim // 2
    dx, dy = (0, -1)

    #populate spiral
    spiral = [[None] * dim for i in range(dim)]

    #fill spiral
    index = 0
    while True:
        index += 1
        spiral[y][x] = index
        turned_dx, turned_dy = turning[dx, dy]
        turned_x = x + turned_dx
        turned_y = y + turned_dy

        if 0 <= turned_x < dim and 0 <= turned_y < dim and spiral[turned_y][turned_x] is None:
            x = turned_x
            y = turned_y
            dx = turned_dx
            dy = turned_dy
        else:
            x += dx
            y += dy
            if not 0 <= x < dim and 0 <= y < dim:
                return spiral

#  Input: grid a 2-D list containing a spiral of numbers
#         val is a number withing the range of numbers in
#         the grid
#  Output: sub-grid surrounding the parameter val in the grid
#          sub-grid could be 1-D or 2-D list
def sub_grid(grid,val):
    x = 0
    y = 0
    #get center value
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == val:
                x = i
                y = j

    #get the surrounding values
    if x == len(grid) - 1 and y == len(grid) - 1:
        val_list = list([x - 1, y - 1, 2, 2])
    elif x == len(grid) - 1 and y == 0:
        val_list = list([x - 1, y, 2, 2])
    elif x == 0 and y == 0:
        val_list = list([x, y, 2, 2])
    elif x == 0 and y == len(grid) - 1:
        val_list = list([x, y - 1, 2, 2])
    elif x == 0:
        val_list = list([x, y - 1, 2, 3])
    elif x == len(grid) - 1:
        val_list = list([x - 1, y - 1, 2, 3])
    elif y == 0:
        val_list = list([x - 1, y, 3, 2])
    elif y == len(grid) - 1:
        val_list = list([x - 1, y - 1, 3, 2])
    else:
        val_list = list([x - 1, y - 1, 3, 3])

    #print surrounding values
    for i in range(val_list[2]):
        for j in range(val_list[3]):
            print(grid[i + val_list[0]][j + val_list[1]], end=' ')
        print('')

def main():
    #prompt user to enter dimension of grid
    dim = int(input('\nEnter dimensions of the grid:'))
    #prompt user to enter value in grid
    val = int(input('Enter value in grid:'))
    print('')
    spiral = create_spiral(dim)
    #print sub grid surrounding value
    sub_grid(spiral, val)
if __name__ == "__main__":
    main()