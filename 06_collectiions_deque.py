from collections import deque
d=deque()
d.append(1)
d.append(2)

d.extendleft([4,5,6])
d.rotate(1)
print(d)