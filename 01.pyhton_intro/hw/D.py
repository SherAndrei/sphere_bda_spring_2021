def calculate(N, K):
    return 0 if K < 1 else int(N * K) + calculate(N, K - 1)


(N, K) = input().split()
print(calculate(N, int(K)))
