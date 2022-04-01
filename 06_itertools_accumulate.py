from itertools import accumulate
import operator
a = [1,2,3,4]
accu = accumulate(a,func=operator.mul)
print(a)
print(list(accu))