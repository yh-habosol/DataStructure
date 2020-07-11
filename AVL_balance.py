class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right  = None
        self.height = 0

    def __str__(self):
        return str(self.key)

    def __iter__(self):
        if self!=None:
            if self.left!=None:
                for elm in self.left:
                    yield elm
                    
            yield self.key
            
            if self.right!=None:
                for elm in self.right:
                    yield elm
        
class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self):
        return " - ".join(str(k) for k in self)

    def __iter__(self):
        return self.root.__iter__()
        
    def preorder(self,v):
        if v!=None:
            print(v, end=' ')
            self.preorder(v.left)
            self.preorder(v.right)
            

    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v, end = ' ')
            self.inorder(v.right)
            

    def postorder(self, v):
        if v!= None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v, end = ' ')

    def find_loc(self, key):
        if self.size ==0:
            return None
        p = None
        v = self.root
        while v!=None:                        
            if v.key ==key:
                return v
            elif v.key<key:
                p = v
                v = v.right
            else:
                p = v
                v = v.left
        return p

    def search(self, key):
        p = self.find_loc(key)
        if p!=None and p.key ==key:
            return p
        else:
            return None


    def insert(self, key):
        p = self.find_loc(key)
        if p ==None or p.key != key:
            v = Node(key)
            if p==None:
                self.root = v
            else:
                v.parent = p
                if p.key<key:
                    p.right = v
                else:
                    p.left = v
            self.size += 1
            return v
        else:
            return None
    
    def deleteByMerging(self,x):
        if x==None:
            return None
        else:
            a, b, pt = x.left, x.right, x.parent
            if a==None:
                c = b
                s = pt
            else:
                c = m = a
                while m.right:
                    m = m.right
                m.right = b
                if b != None:
                    b.parent = m
                s = m
            if x ==self.root:
                if c != None:
                    c.parent = None
                self.root = c
            else:
                if x==pt.left:
                    pt.left = c
                else:
                    pt.right= c
                if c != None:
                    c.parent = pt
            self.size -= 1
            return s

    def deleteByCopying(self, x):
        if x==None:
            return None
        else:
            a, b, pt = x.left, x.right, x.parent
            if a:
                v = a
                while v.right:
                    v = v.right
                x.key = v.key
                if v.parent.left==v:
                    x.left = v.left
                    if v.left:
                        v.left.parent = x
                else:
                    v.parent.right = v.left
                    if v.left:
                        v.left.parent = v.parent
            elif a == None and b:
                v = b
                while v.left:
                    v = v.left
                x.key = v.key
                if v.parent.right == v:
                    x.right = v.right
                    if v.right:
                        v.right.parent = x
                else:
                    v.parent.left = v.right
                    if v.right:
                        v.right.parent = v.parent
            elif a == None and b == None:
                if x == self.root:
                    self.root = None
                    x = None
                else:
                    if x == pt.left:
                        pt.left = None
                        x = pt
                    else:
                        pt.right = None
                        x = pt
                        
            self.size -= 1
            return x

    def rotateRight(self, z):
        if z==None:
            return
        x = z.left
        if x==None:
            return
        b = x.right
        x.parent = z.parent
        if z.parent!=None:
            if z==z.parent.right:
                z.parent.right = x
            else:
                z.parent.left = x
        x.right=z
        z.parent = x
        z.left = b
        if b!=None:
            b.parent = z
        if z==self.root:
            self.root = x

    def rotateLeft(self, z):
        if z ==None:
            return
        x = z.right
        if x==None:
            return
        b = x.left
        x.parent = z.parent
        if z.parent!=None:
            if z== z.parent.left:
                z.parent.left = x
            else:
                z.parent.right = x
        x.left = z
        z.parent = x
        z.right = b
        if b!=None:
            b.parent = z
        if z==self.root:
            self.root = x
        
    
    def succ(self, x):
        if x==None:
            return None
        if x.parent==None:
            if x.right==None:
                return None
            else:
                v = x.right
                while v.left != None:
                    v = v.left
                return v
        elif x==x.parent.left:
            if x.right==None:
                return x.parent
            else:
                v = x.right
                while v.left!=None:
                    v = v.left
                return v
        else:
            if x.right==None:
                v = x.parent
                while v !=None:
                    if v.key<x.key:
                        v = v.parent
                    else:
                        break
                if v==None:
                    return None
                else:
                    return v
            else:
                v = x.right
                while v.left !=None:
                    v = v.left
                return v
                
           

    def pred(self, x):
        if x==None:
            return None
        if x.parent==None:
            if x.left==None:
                return None
            else:
                v = x.left
                while v.right != None:
                    v = v.right
                return v
            
        elif x.parent.right==x:
            if x.left ==None:
                return x.parent
            else:
                v = x.left
                while v.right != None:
                    v = v.right
                return v
        else:
            if x.left ==None:
                v = x.parent
                while v!=None:
                    if v.key>x.key:
                        v = v.parent
                    else:
                        break
                if v==None:
                    return None
                else:
                    return v

            else:
                v = x.left
                while v.right != None:
                    v =v.right
                return v
            
            
    
    def height(self, x):
        if x==None:
            return -1
        else:
            return self.updateHeight(x)

    def updateHeight(self, x):
        if x==None:
            return -1
        
        LH = self.updateHeight(x.left)
        RH = self.updateHeight(x.right)
        if LH>RH:
            return LH+1
        else:
            return RH+1


class AVL(BST):
    def __init__(self):
        self.root = None
        self.size = 0

    def rebalance(self, x, y, z):
        pass
        # assure that x, y, z != None
        # return the new 'top' node after rotations
        # z - y - x의 경우(linear vs. triangle)에 따라 회전해서 균형잡음
        if y==z.left and x == y.left:
            super().rotateRight(z)
            return y
            
        elif y == z.left and x == y.right:
            super().rotateLeft(y)
            super().rotateRight(z)
            return x
            
        elif y == z.right and x == y.right:
            super().rotateLeft(z)
            return y
            
        else:
            super().rotateRight(y)
            super().rotateLeft(z)
            return x
        
            
            

    def insert(self, key):
        
        # BST에서도 같은 이름의 insert가 있으므로, BST의 insert 함수를 호출하려면 
        # super(class_name, instance_name).method()으로 호출
        v = super(AVL, self).insert(key)
        # x, y, z를 찾아 rebalance(x, y, z)를 호출
        if self.root ==v:
            pass
        else:
            p = v.parent
            while p:
                if super().height(p.right) - super().height(p.left) >= 2 or super().height(p.right) - super().height(p.left) <= -2:
                    z = p
                    if super().height(z.right)>super().height(z.left):
                        y = z.right
                    else:
                        y = z.left
                    if super().height(y.right)>super().height(y.left):
                        x = y.right
                    else:
                        x = y.left
                    w = self.rebalance(x,y,z)
                    if w.parent ==None:
                        self.root = w
                    break
                p = p.parent
        return v
        
    def delete(self, u): # delete the node u
        v = super().deleteByCopying(u) # 또는 self.deleteByMerging을 호출
        # height가 변경될 수 있는 가장 깊이 있는 노드를 리턴받아 v에 저장

        while v:
            # v가 AVL 높이조건을 만족하는지 보면서 루트 방향으로 이동
            # z - y - x를 정한 후, rebalance(x, y, z)을 호출
            if super().height(v.right) - super().height(v.left) >= 2 or super().height(v.right) - super().height(v.left) <= -2:
                z = v
                if super().height(z.left)>=super().height(z.right):
                    y = z.left
                else:
                    y = z.right
                if super().height(y.left)>=super().height(y.right):
                    x = y.left
                else:
                    x = y.right
                v = self.rebalance(x,y,z)
            w = v
            v = v.parent
            if v==None:
                self.root = w
        
T = AVL()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'delete':
        v = T.search(int(cmd[1]))
        T.delete(v)
        print("- {0} is deleted".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == 'height':
        h = T.height(T.search(int(cmd[1])))
        if h == -1:
            print("= {0} is not found!".format(cmd[1]))
        else:
            print("= {0} has height of {1}".format(cmd[1], h))
    elif cmd[0] == 'succ':
        v = T.succ(T.search(int(cmd[1])))
        if v == None:
            print("> {0} is not found or has no successor".format(cmd[1]))
        else:
            print("> {0}'s successor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'pred':
        v = T.pred(T.search(int(cmd[1])))
        if v == None:
            print("< {0} is not found or has no predecssor".format(cmd[1]))
        else:
            print("< {0}'s predecssor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
