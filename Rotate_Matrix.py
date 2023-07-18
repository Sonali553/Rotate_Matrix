r, c = map(int, input().split())
lst = []
for i in range(0, r):
    l = list(map(int, input().split()))
    lst.append(l)
def rotate_Matrix(lst):
    r = len(lst)
    c = len(lst[0])
    result = []
    for i in range(0, c):
        res =[]
        for j in range(0, r):
            res.append(lst[j][i])
        result.append(res[::-1])
        
    return result
print(rotate_Matrix([[1, 2], [3, 4]]))
print(rotate_Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))