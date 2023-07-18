r, c = map(int, input().split())
lst = []
for i in range(0, r):
    l = list(map(int, input().split()))
    lst.append(l)
def matrix_Transpose(lst):
    r = len(lst)
    c = len(lst[0])
    result = []
    for i in range(0, c):
        res =[]
        for j in range(0, r):
            res.append(lst[j][i])
        result.append(res)
    return result
print(matrix_Transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(matrix_Transpose([[1, 2],[1, 2], [1, 2]]))
print(matrix_Transpose(lst))