class Node:
	def __init__(self, key=None):
		self.key = key
		self.next = None
	def __str__(self):
		return str(self.key)
	
class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
	
	def __len__(self):
		return self.size
	
	def __iter__(self):
		v=self.head
		while v:
			yield v
			v = v.next
	
	def printList(self): # 변경없이 사용할 것!
		v = self.head
		while(v):
			print(v.key, "->", end=" ")
			v = v.next
	
	def pushFront(self, key):
		newNode = Node(key)
		newNode.next = self.head
		self.head = newNode
		self.size += 1

	def pushBack(self, key):
		newNode = Node(key)
		newNode.next = None
		if self.size==0:
			self.head = newNode
			
		else:
			tail = self.head
			while tail.next!= None:
				tail = tail.next
			tail.next = newNode
		self.size += 1
		
	def popFront(self): 
		# head 노드의 값 리턴. empty list이면 None 리턴
		if self.size==0:
			return None
		else:
			x = self.head
			key = x.key
			self.head = x.next
			del x
			self.size -= 1
			return key
		
	def popBack(self):
		# tail 노드의 값 리턴. empty list이면 None 리턴
		if self.size ==0:
			return None
		else:
			prev, tail = None, self.head
			while tail.next!= None:
				prev = tail
				tail = tail.next
			if prev==None:
				self.head = None
			else:
				prev.next = tail.next
			key = tail.key
			del tail
			self.size -= 1
			return key	
				
	def search(self, key):
		# key 값을 저장된 노드 리턴. 없으면 None 리턴
		for v in self:
			if v.key ==key:
				return v
		return None
	
	def remove(self, x):
		# 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
		if self.size==0 or x==None:
			return False
		elif self.head==x:
			rem = self.head
			self.head = self.head.next
			del rem
			self.size -= 1
			return True
		else:
			prev, rem = None, self.head
			while rem!=x:
				prev = rem
				rem = rem.next
			prev.next = rem.next
			del rem
			self.size -= 1
			return True

	def size(self):
		return self.size

class min_heap:
    def __init__(self, L = []):
        self.A = L

    def __str__(self):
        return str(self.A)

    def heapify_down(self, k, n):
       while 2*k+1<n:
                L,R = 2*k+1, 2*k+2
                if self.A[L][1]<self.A[k][1]:
                    m = L
                else:
                    m = k
                if R<n and self.A[R][1]<self.A[m][1]:
                    m = R
                if m!=k:
                    self.A[k], self.A[m] = self.A[m], self.A[k]
                    k = m
                else:
                    break

                      

    def make_heap(self):
        n = len(self.A)
        for k in range(n-1, -1, -1):
            self.heapify_down(k, n)

    def heapify_up(self, k):
        while k>0 and self.A[(k-1)//2][1] > self.A[k][1]:
            self.A[(k-1)//2] , self.A[k] = self.A[k], self.A[(k-1)//2]
            k = (k-1)//2
        

    def insert(self, key):
        self.A.append(key)
        self.heapify_up(len(self.A)-1)

    def delete_min(self):
        if len(self.A)==0:
            return None
        
        key = self.A[0]
        self.A[0], self.A[-1] = self.A[-1], self.A[0]
        self.A.pop()
        self.heapify_down(0, len(self.A))
        return key



class Graph():
    def __init__(self, n, vertex):
        self.V = vertex
        self.graph = [SinglyLinkedList() for i in range(n)]

    def add_edge(self,u,v,w):
        self.graph[u].pushFront([v,w]) 



def Dijkstra(g):
    maximum = float('inf')
    Q = min_heap()
    dist = [maximum]*len(g.V)
    dist[0] = 0

    def relax(u, v):
        dist
        if dist[v[0]]>dist[u]+v[1]:
            dist[v[0]] = dist[u]+v[1]

    for i in range(len(dist)):
        Q.insert([i,dist[i]])

    while len(Q.A)!=0:
        u = Q.delete_min()
        h = g.graph[u[0]].head
        while True:
            if h ==None:
                break
            relax(u[0],h.key)
            for i in range(len(Q.A)):
                if Q.A[i][0] == h.key[0]:
                    Q.A[i][1] = dist[h.key[0]]
                    Q.heapify_up(i)
                    break
            h = h.next
            if h ==None:
                break
    return dist
        

def main():
    n = int(input())
    m = int(input())
    
    v_list = [i for i in range(n)]

    g = Graph(n, v_list)
    for i in range(m):
        a, b, c = map(int, input().split())
        g.add_edge(a,b,c)

    dist = Dijkstra(g)
    for i in dist:
        print(i, end=' ')

main()
