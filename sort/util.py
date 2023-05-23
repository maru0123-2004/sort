def isSorted(lst):
    now=lst[0]
    for i in lst:
        if now > i:
            return False
    else:
        return True
def checkit(func):
    import random, time
    from pprint import pprint
    #a=random.sample(range(0, 10**10), random.randint(10,1000))
    a=[20,6,55,74,3,45,13,87,46,30]
    t1=time.process_time()
    b=sorted(a)
    t2=time.process_time()
    a=func(a)
    t3=time.process_time()
    pprint(a, compact=True)
    print("builtin sort function check:", a==b, "| isSorted check:", isSorted(a),  "| builtin sort's query time:", t2-t1, "| query time:", t3-t2, "s")

