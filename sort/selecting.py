def legacy_min(lst):
    lowest=lst[0]
    for num in lst:
        if num < lowest:
            lowest=num
    return lowest

def select(lst):
    for i in range(len(lst)):
        idx=lst.index(legacy_min(lst[i:]))
        lst[i], lst[idx]=lst[idx], lst[i]
    return lst

if __name__ == "__main__":
    from util import checkit
    checkit(select)
