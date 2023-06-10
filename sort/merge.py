def merge(lst):
    if len(lst)>2: lst[:len(lst)//2], lst[len(lst)//2:]=merge(lst[:len(lst)//2]), merge(lst[len(lst)//2:])
    if len(lst)>=2:
        l=[]
        for i, j in zip(lst[:len(lst)//2], lst[len(lst)//2:]):
            if i<j:
                l.append(i)
                l.append(j)
            else:
                l.append(j)
                l.append(i)
        return l
    else:
        return lst

if __name__ == "__main__":
    from util import checkit
    checkit(merge)