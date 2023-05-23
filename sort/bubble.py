def bubble(lst):
    for j in range(len(lst)):
        for i in range(len(lst)-1,0,-1):
            if lst[i]<lst[i-1]:
                lst[i], lst[i-1] = lst[i-1], lst[i]
    return lst

if __name__ == "__main__":
    from util import checkit
    checkit(bubble)
