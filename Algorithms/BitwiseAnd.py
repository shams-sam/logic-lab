# https://www.hackerrank.com/challenges/linkedin-practice-bitwise-and
# for a given number k, k-1 is the most optimal solution
# so for achieving k-1 we need a & b where a,b belong to set {1..n}
# since bitwise and results are less than or equal to operands
# to achieve k-1 let a be k-1 and then the other number b should be k-1|k
# because k & (k|k+1) = k
# now we need to check if  k|k-1 is in the set {1..n} or not
# k|k-1 = k if k is odd
# if k is even, then if k|k-1 lies in {1..n} then k-1 is the answer
# else because k-1 is odd k-2 would definitely be achievable
t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    print(k-1 if ((k-1)|k <= n) else k-2)
