n = int(input())

def factorial(ans, a):
    if a == 0:
        return ans
    else:
        return factorial(ans * a, a - 1)

if n == 0:
    print(1)
else:
    print(factorial(1, n))