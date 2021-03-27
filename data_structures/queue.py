'''
Queue:
    rear -> insertion at rear end
    front -> deletion at front end
    size -> current size of queue
    capacity -> max capacity of queue
    q -> data structure/array which holds elements of queue
'''

class Queue:
    def __init__(self, capacity):
        self.rear = -1
        self.front = self.size = 0
        self.capacity = capacity
        self.q = [None] * capacity
        print("Queue Initiliased")
        return

    def full(self):
        return self.size == self.capacity

    def empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.full():
            print("Queue overflow, increase max capacity")
            return
        self.rear = self.rear + 1
        self.q[self.rear] = item
        self.size = self.size + 1
        print(f"Enqueued successfully, {self.q[self.rear]}")
        return self.q
    
    def dequeue(self):
        if self.empty():
            print("Queue underflow, no elements present")
            return

        print(f"Dequeued successfully, {self.q[self.front]}")
        self.q[self.front] = None
        self.front = self.front + 1
        self.size = self.size - 1
        

    def get_rear(self):
        if self.empty():
            print("Queue empty, no elements present")
            return
        print(f"Recent item added in is, {self.q[self.rear]}")

    def get_front(self):
        if self.empty():
            print("Queue empty, no elements present")
            return
        print(f"Least recent item added in is, {self.q[0]}")

    def display(self):
        if self.empty():
            print("Queue empty, no elements present")
            return
        print
        print ("-------------------------")
        print(self.q[::-1])
        print ("-------------------------")

if __name__ == '__main__':
    queue = Queue(5)

    # Enqueue check
    for k in [1, 2, 3, 4, 5]:
        queue.enqueue(k)
        queue.display()

    # Recent item check
    queue.get_rear()
    queue.display()

    # Least recent item check
    queue.get_front()
    queue.display()

    # Overflow check
    queue.enqueue(6)
    queue.display()

    # Dequeue check
    for k in [1, 2, 3, 4, 5]:
        queue.dequeue()
        queue.display()

    # Underflow check
    queue.dequeue()
    queue.display()

    

    

