# Queue: A queue.
# Your implementation should pass the tests in test_queue.py.
# Abhimanyu, bais

# Hint:
#

from llist import sllist

class Queue:

    def __init__(self):
        self.data = sllist()

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.popleft()

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False



        #pass

