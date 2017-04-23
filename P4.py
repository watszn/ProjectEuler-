# Find the largest palindrome made from the product of two 3-digit numbers

def palindrome_count(n):
    n = str(n)
    if len(n) <= 1:
        return 0
    if n[0] == n[-1]:
        return 1 + palindrome_count(n[1:len(n) - 1])
    else:
        return 0 + palindrome_count(n[1:len(n) - 1])


def main():

    count = 0 # highest palindrome count
    largest_palindrome = 0
    d1, d2 = 0, 0
    for i in range (100, 1000):
        for j in range (100, 1000):
            if (palindrome_count(i * j) >= count) and ((i * j) > largest_palindrome):
                largest_palindrome = i * j
                count = palindrome_count(i * j)
                d1, d2 = i, j
    print (count)
    print (d1, d2, d1 * d2)




main()
