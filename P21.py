def amicable(n):
    a_sum = 0
    for i in range (1, int((n * 0.5)) + 1):
        if n % i == 0:
            a_sum += i
    return a_sum

if __name__ == '__main__':
    a = 0
    for i in range (1, 10000):
        output = amicable(i)
        if amicable(output) == i and i != output:
            a += i
            print ('amicable number found: %s and %s' % (i, output))
    print (a)
