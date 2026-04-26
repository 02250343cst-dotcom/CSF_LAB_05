class Queue:
    def __init__(self):
        self.queue = []
 
    def enqueue(self, item):
        self.queue.append(item)
 
    def dequeue(self):
        return self.queue.pop(0) if self.queue else None
 
    def front(self):
        return self.queue[0] if self.queue else None
 
    def is_empty(self):
        return len(self.queue) == 0
 
    def display(self):
        return self.queue
 
# Test
q = Queue()
q.enqueue(100)
q.enqueue(200)
q.enqueue(300)
print(f"Queue: {q.display()}")
print(f"Front: {q.front()}")
print(f"Dequeued: {q.dequeue()}")
print(f"After: {q.display()}")
 