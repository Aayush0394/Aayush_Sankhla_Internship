def Prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
n=7
if Prime(7):
    print(f"{n} is Prime")
else:
    print(f"{n} is composite")
