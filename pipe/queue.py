class Full(Exception): pass
class Empty(Exception): pass

class Queue():
    def __init__(self, length):
        self.list=[None for i in range(length)]
        self.rearpointer=0
    def enqueue(self, data):
        if len(self.list) <= self.rearpointer:
            raise Full
        self.list[self.rearpointer]=data
        self.rearpointer+=1
    def dequeue(self):
        if self.rearpointer<=0:
            raise Empty
        temp,*self.list=*self.list, None
        self.rearpointer-=1
        return temp