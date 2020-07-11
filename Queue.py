class Queue:
    def __init__(self):
        self.items = []
        self.front_index = 0

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if self.front_index==len(self.items):
            print("Queue is Empty")
        else:
            x = self.items[self.front_index]
            self.front_index += 1
            return x
    




