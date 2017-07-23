def main():
    in_file = open('./P67.txt', "r")
    tri = []
    for line in in_file:
        line = line.strip()
        line = line.split()
        line = [int(i) for i in line]
        tri.append(line)
    print (tri)
    for row in range (len(tri) - 2, -1, -1):
        for column in range (row + 1):
            print ('%s largest leaf is %s' % (tri[row][column],max(tri[row + 1][column], tri[row + 1][column + 1]) ))
            tri[row][column] += max(tri[row + 1][column], tri[row + 1][column + 1]) # add largest leaf directly below

    print (tri[0][0])


main()
