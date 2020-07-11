class Heap:
    def __init__(self, L=[]):
        self.A = L

    def __str__(self):
        return str(self.A)

    def heapify_down(self, k, n):
        while 2*k+1 < n:
            L, R = 2*k+1, 2*k+2
            if R >= n:
                if max(self.A[k], self.A[L]) != self.A[k]:
                    self.A[k], self.A[L] = self.A[L], self.A[k]
                    k = L
                else:
                    break
            else:
                if max(self.A[k], self.A[L], self.A[R]) != self.A[k]:
                    if self.A[R] > self.A[L]:
                        self.A[R], self.A[k] = self.A[k], self.A[R]
                        k = R
                    else:
                        self.A[L], self.A[k] = self.A[k], self.A[L]
                        k = L
                else:
                    break

    def make_heap(self):
        n = len(self.A)
        for k in range(n-1, -1, -1):
            self.heapify_down(k, n)

    def heapify_up(self, k):
        while k > 0 and self.A[(k-1)//2] < self.A[k]:
            self.A[(k-1)//2], self.A[k] = self.A[k], self.A[(k-1)//2]
            k = (k-1)//2

    def insert(self, key):
        self.A.append(key)
        self.heapify_up(len(self.A)-1)

    def delete_max(self):
        if len(self.A) == 0:
            return None

        key = self.A[0]
        self.A[0], self.A[-1] = self.A[-1], self.A[0]
        self.A.pop()
        self.heapify_down(0, len(self.A))
        return key

    def heap_sort(self):
        # 내림차순 정렬
        '''
        B = []
        for i in range(len(self.A)):
            B.append(self.delete_max())
        self.A = B
        '''
        # 오름차순 정렬
        n = len(self.A)
        for k in range(n-1, -1, -1):
            self.A[0], self.A[k] = self.A[k], self.A[0]
            n = n-1
            self.heapify_down(0, n)
