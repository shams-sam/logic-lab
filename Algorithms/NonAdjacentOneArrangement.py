# program to find the number of arrangements
# using digits 1 and 0
# such that given an array of size m
# no two cells having 1 are adjacent
# travelyaari

class non_adjacent_one_arrangement():
    def get_sum(self, m):
        values = self.calc(m)
        return values[0] + values[1]

    def calc(self, m):
        if m == 1:
            return [1, 1]
        values = self.calc(m-1)
        return [values[1]+values[0], values[0]]


def main():
    arr = non_adjacent_one_arrangement()
    m = raw_input('M:')
    print arr.get_sum(int(m))

if __name__ == '__main__':
    main()