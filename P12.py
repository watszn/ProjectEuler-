# solution to P12

def tri_num(n):
    return int ((n * (n + 1)) / 2)

def tri_divisor(n):
    divisor = 0
    for i in range (1, int((n ** 0.5)) + 1):
        if n % i == 0:
            divisor += 1
    return divisor * 2

def main():

    n = 28
    i = 7
    while tri_divisor(n) < 500:
        print ('%d has %d divisors' % (n, tri_divisor(n)))
        i += 1
        n = tri_num(i)
    print (n)

main()
