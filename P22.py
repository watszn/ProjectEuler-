from string import ascii_uppercase

if __name__ == '__main__':
    in_file = open('./P22.txt', 'r')
    in_file = in_file.read()
    in_file = in_file.strip()
    in_file = in_file.strip(',')
    in_file = in_file.split(",")
    name_list = [name.replace('\"', '') for name in in_file]
    name_list = sorted(name_list)
    # create dict of alpha and value
    letter_dict = {}
    total = 0
    for count, letter in enumerate(ascii_uppercase):
        letter_dict[letter] = count + 1
    for count, name in enumerate(name_list, start = 1):
        t = 0 # name count
        for letter in name:
            t += letter_dict[letter]
        _t = t * count
        total += _t
    print (total)
