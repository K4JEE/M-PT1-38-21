l=[1,2,3,4,5,8,9,10,12,14]
def get_ranges(l):
    n=0
    for i in range(1,len(l)):
        if l[i]>1+l[i-1]:
            yield  (l[i],l[i-1])
    yield (l[i], l[-1])
print(str(', '.join(['%d'% a if a == b else '%d-%d'%(a,b) for (a,b)in get_ranges(l)])))
