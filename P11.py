# Solution to Project Euler #11
def hor_sum(num_list):
    product = 1
    for row in range (len(num_list)):
        temp = 1
        for column in range (len(num_list[row])):
            temp *= num_list[row][column]
        product = max(product, temp)
    return product

def vert_sum(num_list):
    product = 1
    for row in range (len(num_list)): # check # of row
        temp = 1
        row_list = num_list[row]
        try:
            for column in range (len(num_list[row])):
                temp *= num_list[column][row]
            product = max(product, temp)
        except IndexError:
            continue
    return product

def diagonal_sum(num_list):
    product = 1
    for row in range (len(num_list)):
        rtemp = 1
        ltemp = 1
        try:
            for column in range (len(num_list[row])):
                rtemp *= num_list[column][column]
                ltemp *= num_list[len(num_list[row]) - column - 1][column]
            product = max(product, rtemp)
            product = max(product, ltemp)
        except IndexError:
            continue
    return product

def window(num_list, r, c, length): # matrix in a selected scope denoted by length
    w = []
    for i in range (length):
        temp = []
        for j in range (length):
            if c + j < len(num_list[r]) and r + i < len(num_list):
                temp.append(num_list[r + i][c + j])
        w.append(temp)
    return w

if __name__ == "__main__":
    in_file = open('./P11.txt', 'r')
    grid = []
    gp = 0 # greatest product
    for line in in_file:
        line = line.strip()
        line = line.split()
        line = [int(i) for i in line]
        grid.append(line)
    for row in range (len(grid)):
        for column in range (len(grid[row])):
            scope = window(grid, row, column, 4)
            gp = max(gp, hor_sum(scope), vert_sum(scope), diagonal_sum(scope))
    print (gp)
