if __name__ == "__main__":
    from insert import insert
else:
    from .insert import insert

def shell(lst):
    for i in range(len(lst)//2, 0, -1):
        for j in range(i):
            lst[j::i]=insert(lst[j::i])
    return lst

if __name__ == "__main__":
    from util import checkit
    checkit(shell)