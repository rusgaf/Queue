class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        else:
            elem = self.queue[0]
            del self.queue[0]
            return elem

    def size(self):
        return len(self.queue)
