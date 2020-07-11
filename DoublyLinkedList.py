class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = self
        self.prev = self

    def __str__(self):
        return str(self.key)


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def __iter__(self):
        v = self.head.next
        while v != self.head:
            yield v
            v = v.next

    def __str__(self):
        return " -> ".join(str(v) for v in self)

    def __len__(self):
        return self.size

    def printList(self):
        v = self.head.next
        print("h ->", end=" ")
        while v != self.head:
            print(v.key, "->", end=" ")
            v = v.next
        print("h")

    def splice(self, a, b, x):
        if a == None or b == None or x == None:
            return
        ap = a.prev
        bn = b.next

        ap.next = bn
        bn.prev = ap

        xn = x.next
        x.next = a
        a.prev = x
        b.next = xn
        xn.prev = b

    def search(self, key):
        tem = self.head.next
        while tem != self.head:
            if tem.key == key:
                return tem
            tem = tem.next
        return None

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def first(self):
        if self.size == 0:
            return None
        else:
            return self.head.next

    def last(self):
        if self.size == 0:
            return None
        else:
            return self.head.prev

    def moveAfter(self, a, x):
        self.splice(a, a, x)

    def moveBefore(self, a, x):
        self.splice(a, a, x.prev)

    def insertAfter(self, x, key):
        self.moveAfter(Node(key), x)
        self.size += 1

    def insertBefore(self, x, key):
        self.moveBefore(Node(key), x)
        self.size += 1

    def pushFront(self, key):
        self.insertAfter(self.head, key)

    def pushBack(self, key):
        self.insertBefore(self.head, key)

    def deleteNode(self, x):
        if x == None or self.head == x:
            return
        x.prev.next, x.next.prev = x.next, x.prev
        del x
        self.size -= 1

    def popFront(self):
        if self.isEmpty():
            return None
        key = self.head.next.key
        self.deleteNode(self.head.next)
        return key

    def popBack(self):
        if self.isEmpty():
            return None
        key = self.head.prev.key
        self.deleteNode(self.head.prev)
        return key
