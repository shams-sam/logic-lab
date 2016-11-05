n, d = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
for i in xrange(n):
    print str(a[(i+d)%n]) + ' ',
