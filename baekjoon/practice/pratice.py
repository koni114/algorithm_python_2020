def prime(N):
    if N < 2: return False
    for i in range(2, (N//2)+1):
        if N % i == 0: return False
    return True



