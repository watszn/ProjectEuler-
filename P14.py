# solution to P14

def num(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3*n + 1

def largest_collatz(n, c, d): # c is count
    if num(n) == 1: # base case
        c += 1
        return c
    elif num(n) in d:
        return c + d[num(n)]
    else:
        n = num(n)
        return largest_collatz(n, c + 1, d)

def main():
    # num : chain
    chain = {1: 0}
    largest_chain, val = 0, 0
    for i in range (2, 1000001):
        chain[i] = largest_collatz(i, 1, chain)
        if chain[i] > largest_chain:
            val = i
            largest_chain = max(chain[i], largest_chain)
    print (val)

main()
