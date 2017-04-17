# Project Euler Q3.

def is_prime(n):
    for i in range (1, n + 1):
        if i != 1 and i != n:
            if n % i == 0:
                return False
    return True

def LPF(n):
    LPF = 0
    for i in range (n // 2, 1, -1):
        if is_prime(i) and n % i == 0:
            LPF = i
            return LPF
        else:
            continue

def main():

    print (LPF(600851475143))


main()
