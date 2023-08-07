class StackOverflow(Exception): pass
class StackUnderflow(Exception): pass

class Stack():
    def __init__(self, length):
        self.list=[None for i in range(length)]
        self.pointer=0
    def push(self, data):
        if len(self.list) <= self.pointer:
            raise StackOverflow
        self.list[self.pointer]=data
        self.pointer+=1
    def pop(self):
        if self.pointer<=0:
            raise StackUnderflow
        self.pointer-=1
        temp=self.list[self.pointer]
        self.list[self.pointer]=None
        return temp