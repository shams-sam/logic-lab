# given a number print all perfect fractions
# starting with 0/1 and ending with 1/1
# example input : 4
# output : [0 / 1] [1 / 4] [1 / 3] [1 / 2] [2 / 3] [3 / 4] [1 / 1]
# catamaran ventures

def swap_numbers(a,b):
    return (b,a)

def calculate_value(array):
    return float(array[0])/float(array[1])

def sort(array, start, end, payload):
    if start < end:
        j = start
        p = end
        for i in xrange(start, end+1):
            if array[i] <= array[p]:
                array[i], array[j] = swap_numbers(array[i], array[j])
                payload[i], payload[j] = swap_numbers(payload[i], payload[j])
                j += 1
        sort(array, start, j-2, payload)
        sort(array, j, end, payload)

def get_fractions(number):
    fraction_list = []
    for i in xrange(2, number+1):
        for j in xrange(1, i):
            if i%j != 0 or j == 1:
                fraction_list.append([j,i])
    return fraction_list

def main():
    number = map(int, raw_input("Number: "))
    fractions = get_fractions(number[0])
    fractions = fractions + [[0,1], [1,1]]
    fraction_values = map(calculate_value, fractions)
    sort(fraction_values, 0, len(fractions)-1, fractions)
    for elem in fractions:
        print '[', elem[0], '/', elem[1], ']',

main()
