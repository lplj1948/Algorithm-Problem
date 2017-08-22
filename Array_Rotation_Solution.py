'''
Array Rotation Solution


A = [3, 8, 9, 7, 6]
K = 3  

print array_right_rotation(A,len(A),K)
print array_left_rotation(A,len(A),K)

'''

def array_left_rotation(a, n, k):   
    alist = list(a)
    b = alist[k%n:]+alist[:k%n]
    return b

def array_right_rotation(a, n, k):
    alist = list(a)
    b = alist[n-(k%n):]+alist[:n-(k%n)]
    return b


