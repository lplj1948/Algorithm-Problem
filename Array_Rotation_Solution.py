'''
Array Rotation Solution
'''

def array_left_rotation(a, n, k):   
    return a[k%n:]+a[:k%n]

def array_right_rotation(a, n, k):
    return a[n-(k%n):]+a[:n-(k%n)]

    
A = [3, 8, 9, 7, 6]
K = 3  

print array_right_rotation(A,len(A),K)
print array_left_rotation(A,len(A),K)
