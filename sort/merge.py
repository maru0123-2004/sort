def merge(lst):
    for k in range(len(lst)):
        l=[]
        a, b=lst[0::2], lst[1::2]
        for i in range(len(lst)):
            if not (len(a) and len(b)):
                l.extend(a)
                l.extend(b)
                break
            if a[0]<b[0]:
                l.append(a[0])
                del a[0]
            else:
                l.append(b[0])
                del b[0]
        lst=l
    return l

if __name__ == "__main__":
    from util import checkit
    checkit(merge)