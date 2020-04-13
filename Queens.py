#File: Queens.py

#Description: Outputs the solutions for different dimensions of Queens problem

#Student Name: Jaeho Jang

#Course Name: CS 313E

#Unique Number: 50300

#Date Created: 3/12/20

#Date Last Modified: 3/12/20

class Queens(object):
    # initialize the board
    def __init__(self, n=8):
        self.board = []
        self.n = n
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('*')
            self.board.append(row)
        self.solutions = []

    # appends the board to a list of all board solutions
    def append_board(self):
        curr_board = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append(self.board[i][j])
            curr_board.append(row)
        self.solutions.append(curr_board)

    # prints the board solutions and number of total solutions
    def print_board(self):
        for i in range(len(self.solutions)):
            for j in range(self.n):
                for l in range(self.n):
                    print(self.solutions[i][j][l], end=' ')
                print()
            print()
        if len(self.solutions) == 1:
            print('There is one solution for a',self.n,'x',self.n,'board.')
        else:
            print('There are',len(self.solutions),'solutions for a',self.n,'x',self.n,'board.')

    # check if no queen captures another
    def is_valid(self, row, col):
        for i in range(self.n):
            if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
                return False
        for i in range(self.n):
            for j in range(self.n):
                row_diff = abs(row - i)
                col_diff = abs(col - j)
                if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
                    return False
        return True

    # do a recursive backtracking solution
    def recursive_solve(self, col):
        if (col == self.n):
            self.append_board()
        else:
            for i in range(self.n):
                if (self.is_valid(i, col)):
                    self.board[i][col] = 'Q'
                    self.recursive_solve(col + 1)
                    self.board[i][col] = '*'
            return False

    # if the problem has a solution print the board
    def solve(self):
        while self.recursive_solve(0):
            continue
        self.print_board()


def main():
    # prompt and verify user input
    n=int(input('Enter the size of board: '))
    print('')
    while n < 1 or n > 8:
        print('Invalid input.')
        n = int(input('Enter a valid size: '))
        print('')

    game = Queens(n)

    # place the queens on the board
    game.solve()
main()