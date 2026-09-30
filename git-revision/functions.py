a=[1,2,3,4,5]
print(list(filter(lambda i:i%2==0,a)))
from functools import reduce
print(reduce(lambda x,y:x*y,a))
print(list(enumerate(a,start=101)))