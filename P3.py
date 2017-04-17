# Project Euler Q3.

def main():
    n = 600851475143
    i = 2
    while i * i < n: # largest prime factor will not exceed

        while n % i == 0:
            n = n // i
        i += 1
    print (n)

main()
