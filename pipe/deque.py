class Full(Exception): pass
class Empty(Exception): pass

class Deque():
    def __init__(self, length):
        self.list=[None for i in range(length)]
        self.rearpointer=0
    def renqueue(self, data):
        if len(self.list) <= self.rearpointer:
            raise Full
        self.list[self.rearpointer]=data
        self.rearpointer+=1
    def lenqueue(self, data):
        if len(self.list) <= self.rearpointer:
            raise Full
        *self.list, _=data, *self.list
        self.rearpointer+=1
    def ldequeue(self):
        if self.rearpointer<=0:
            raise Empty
        temp,*self.list=*self.list, None
        self.rearpointer-=1
        return temp
    def rdequeue(self):
        if self.rearpointer<=0:
            raise Empty
        self.rearpointer-=1
        temp=self.list[self.rearpointer]
        self.list[self.rearpointer]=None
        return temp