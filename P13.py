# solution to P13


def main():
    in_file = open('./P13.txt', 'r')
    l = []
    for line in in_file:
        line = line.strip()
        line = int(line)
        l.append(line)

    total = 0
    for num in l:
        total += num

    t = str(total)
    print (t[0:10])


main()
