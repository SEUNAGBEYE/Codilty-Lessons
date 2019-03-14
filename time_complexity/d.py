def solution(M, A):
    N = len(A)
    count = [0] * (M + 1)
    maxOccurence = 1
    index = -1
    for i in range(N):
        print(count, i, A[i], count[A[i]])
        if count[A[i]] > 0:
            tmp = count[A[i]]
            if tmp > maxOccurence:
                maxOccurence = tmp
                index = i
            count[A[i]] = tmp + 1
        else:
            count[A[i]] = 1
    return A[index]

print(solution(3, [1, 2, 3, 3, 1, 3, 1]))

# print(solution(3, [1, 2, 3, 3, 1, 3, 1]))