def insert(lst):
    for i in range(1, len(lst)):
        for j in range(i):
            if lst[i]<lst[j]:
                for k in range(i, j , -1):
                    lst[k], lst[k-1]=lst[k-1], lst[k]
    return lst 

if __name__ == "__main__":
    from util import checkit
    checkit(insert)
