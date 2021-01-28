A = [2,4,5,6,7,10]
while True :
    for i in range(len(A)):
        for j in range(1,len(A)):
            if A[i] < A[j]:
                T = A [i]
                A[i] = A [j]
                A[j] = T
print(A)