# Problem 6 on Project Euler

def main():
    # create list range 1-100
    num_list = [x for x in range (1, 101)]
    # create list of sq sum
    sq_sum = [(x**2) for x in num_list]

    a = 0 # sum of range 1-100
    for num in num_list:
        a += num

    b = 0 # sum of all sq num 
    for num in sq_sum:
        b += num

    print ("difference is %s" % ((a**2) - b))


main()
