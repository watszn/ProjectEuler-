# solution to problem 9 from Project Euler
import math

def main():
    p = 1
    for a in range (1, 1000):
        for b in range (a, 1000):
            c = math.sqrt(a**2 + b**2)
            if a + b + c == 1000:
                print ('%d + %d + %d = 1000' % (a, b, c))

    print ('product is %d' %(p))
main()
