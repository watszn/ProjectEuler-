# solution to project euler P7

def check_prime(n):
    for i in range (2, int(n * 0.5) + 1):
        if n % i == 0:
            return True # number is not prime
    return False # number is prime
def main():

    prime_count = 0
    num = 2
    prime_list = []
    while (prime_count <= 10001):
        if not check_prime(num):
            prime_list.append(num)
            prime_count += 1
        num += 1
    print (prime_list[10000])

main()
