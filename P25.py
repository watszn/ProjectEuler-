# solution to P25

def fib(n, mem = {}):
    if n == 1 or n == 2:
        return 1
    if (n - 1) in mem and (n - 2) in mem:
        return mem[n - 1] + mem[n - 2]
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    i = 12
    fib_dict = {}
    while len(str(fib(i, fib_dict))) < 1000:
        fib_dict[i] = fib(i, fib_dict)
        i += 1
    print ("%s term: %s" %(i, fib(i, fib_dict)))
main()
