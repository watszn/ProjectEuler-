# project euler P5
# smallest multiple that is evenly divisible by numbers 1-20

# 2, 4, 6, 8, 10, 12, 14, 16, 18
# 3, 9
# 5, 15, 20
# 7, 11, 13, 17, 19
import time


def smallest_multiple(a, b): # a = list; b = num
    div_evenly = True
    for num in a:
        if b % num != 0:
            div_evenly = False
            break
    return div_evenly

def main():
    start_time = time.time()
    # create list 1 - 20
    num_list = []
    for num in range (1, 21):
        num_list.append(num)
    print (num_list)

    num = 2520
    while (smallest_multiple(num_list, num) == False):
        num += 1
    print (num)
    print ("program takes %s seconds" % (time.time() - start_time))
main()
