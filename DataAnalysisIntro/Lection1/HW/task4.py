def calculate(N, K):
    if (K >= 1):
        return int(N*K) + calculate(N, K - 1)
    return 0


(N, K) = input().split()
print(calculate(N, int(K)))
