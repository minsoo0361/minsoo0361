def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    arr = []
    for i in range(len(A)):
        arr.append(A[i] * B[i])
    answer = sum(arr)    
    return answer