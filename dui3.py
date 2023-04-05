import queue
import random
#q = queue.PriorityQueue()
q = queue.PriorityQueue()
class Node:
    def __init__(self, x):
        self.x = x
    def __lt__(self, other):
        return other.x > self.x
    def __str__(self):
        return "{}".format(self.x)
a = [Node(int(random.uniform(0, 10))) for i in range(10)]
for i in a:
    print(i, end = ' ')
    q.put(i)
print('------------------------')
while q.qsize():
    print(q.get(), end=' ')
