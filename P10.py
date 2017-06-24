# Project Euler Problem 10
def main():
    # sieves of eratosthenes
    value = 0
    n = 2000000
    is_prime = (n + 1) * [True]
    for i in range (2, n + 1):
        if is_prime[i]:
            for j in range (2 * i, n + 1, i):
                is_prime[j] = False

    for prime in range (2, len(is_prime)):
        if is_prime[prime] == True:
            print (prime)
            value += prime
    print (value)

main()
