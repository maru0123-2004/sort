def insert(lst):
    for i in range(1, len(lst)):
        for j in range(i):
            if lst[i]<lst[j]:
                for k in range(i, j , -1):
                    lst[k], lst[k-1]=lst[k-1], lst[k]
    return lst 

if __name__ == "__main__":
    import random, time
    from pprint import pprint
    from __init__ import isSorted
    a=random.sample(range(0, 10**10), random.randint(10,1000))
    #a=[20,6,55,74,3,45,13,87,46,30]
    t1=time.process_time()
    b=sorted(a)
    t2=time.process_time()
    a=insert(a)
    t3=time.process_time()
    pprint(a, compact=True)
    print("builtin sort function check:", a==b, "| isSorted check:", isSorted(a),  "| builtin sort's query time:", t2-t1, "| query time:", t3-t2, "s")
