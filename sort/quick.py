def quick(lst):
    i=0
    j=len(lst)-2
    while(1):
        while lst[i]<lst[-1]: i+=1
        while lst[j]>lst[-1] and i<j: j-=1
        if i>=j: break
        lst[i], lst[j] = lst[j], lst[i]
    lst[i], lst[-1] = lst[-1], lst[i]
    if len(lst[:i])>=3: lst[:i]=quick(lst[:i])
    if len(lst[j+1:])>=3: lst[j+1:]=quick(lst[j+1:])
    
    return lst

if __name__ == "__main__":
    from util import checkit
    checkit(quick)