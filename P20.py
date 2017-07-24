# Solution to P20
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
        
if __name__ == '__main__':
    f = str(factorial(100))
    l = [int(i) for i in f]
    f_sum = 0
    for num in l:
        f_sum += num
    print (f_sum)
