def isSorted(lst):
    now=lst[0]
    for i in lst:
        if now > i:
            return False
    else:
        return True