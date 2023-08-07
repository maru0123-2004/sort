def tree(lst:list):
    n=100
    while n!=0:
        n=0
        for pindex in range(len(lst)//2-1, -1, -1):
            if len(lst)<=pindex*2+2:
                cindex=pindex*2+1
            else:
                if lst[pindex*2+1] > lst[pindex*2+2]:
                    cindex=pindex*2+1
                else:
                    cindex=pindex*2+2
            if lst[cindex]>lst[pindex]:
                lst[pindex],lst[cindex]=lst[cindex],lst[pindex]
                n+=1
    return lst
def heap(lst:list):
    lst=tree(lst)
    lst2=[]
    for i in range(len(lst)):
        lst2.insert(0,lst[0])
        lst[0]=lst[-1]
        del lst[-1]
        lst=tree(lst)
    return lst2

if __name__ == "__main__":
    from util import checkit
    checkit(heap)