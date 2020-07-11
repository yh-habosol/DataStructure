import math


class HashOpenAddr:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None]*self.size
        self.values = [None]*self.size

    def __str__(self):
        s = ""
        for k in self:
            if k == None:
                t = "{0:5s}|".format("")
            else:
                t = "{0:-5d}|".format(k)
            s = s + t
        return s

    def __iter__(self):
        for i in range(self.size):
            yield self.keys[i]

    def set(self, key, value=None):
        # key값 갖는 item이 table에 있으면 update, 없으면 추가
        # 성공하면 key return, 실패하면 full return

        i = self.find_slot(key)
        if i == None:
            return None
        if self.keys[i] != None:
            self.values[i] = value
        else:
            self.keys[i] = key
            self.values[i] = value
        return key

    def find_slot(self, key):
        # key값을 같은 item의 슬롯 번호 리턴

        i = self.hash_function(key)
        start = i
        while self.keys[i] != None and self.keys[i] != key:
            i = (i+1) % self.size
            if i == start:
                return None
        return i

    def remove(self, key):
        # key값 갖는 item 찾음
        # 비어있으면 None return
        # 존재하면 그 칸 비우고 어떤 item으로 채울지 찾아야함

        i = self.find_slot(key)
        if self.keys[i] == None:
            return None
        j = i

        while True:
            self.keys[i] = None
            self.values[i] = None
            while True:
                j = (j+1) % self.size
                if self.keys[j] == None:
                    return key
                k = self.hash_function(self.keys[j])
                if not(i < k <= j or j < i < k or k <= j < i):
                    break
            self.keys[i] = self.keys[j]
            self.values[i] = self.values[j]
            i = j

    def search(self, key):
        i = self.find_slot(key)
        if self.keys[i] != None:
            return self.keys[i]
        else:
            return None

    def hash_function(self, key):
        return abs(key) % self.size

    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, value):
        self.set(key, value)
