# Project Euler Q2.

def fib(n):
    fib_sequence = [0 , 1]
    num1 = 0
    num2 = 1
    for i in range (2, n + 1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

    return (fib_sequence[n])


def main():
    even_sum = 0
    i = 0
    while fib(i) < 4000000:
        if fib(i) % 2 == 0:
            even_sum += fib(i)
            i += 1
        else:
            i += 1
    print (even_sum)

main()
