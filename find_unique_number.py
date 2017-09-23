def lonely_integer(a):
    dic = {}
    
    for i in range(0,n):
        if dic.get(a[i]) == None:
            dic[a[i]] = 1
        else:
            dic[a[i]] += 1
            
    for k,v in dic.items():
        if v == 1:
            return k
   
    return None

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a)