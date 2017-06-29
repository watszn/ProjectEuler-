# solution to Project Euler #16

def main():
    x = str(2 ** 1000)
    s = 0
    for num in x:
        s += int(num)
    print (s)


main()
