# solution for P8 on Project Euler

def multiply_adj(n):
    index = 13
    max_num = 0 # greatest multiple of 13 adjecent nums
    for num in range (len(n)):
        temp = 1
        if index + num <= len(n):
            for i in n[num: num + index]:
                print (i, end = ' ')
                temp *= int(i)
            print ()
            if temp > max_num:
                max_num = temp
                print (max_num)
        else:
            break
    return max_num


def main():

    in_file = open("./P8.txt", "r")
    # create list of numbers
    string = str()
    for line in in_file:
        string += line.strip()
    print (multiply_adj(string))

    # find the max multiple of 13 adjecent nums
main()
