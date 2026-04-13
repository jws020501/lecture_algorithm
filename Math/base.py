def convertBase(n, base):
    result = ""
    digits = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result

n = int(input())
base = int(input())

print(convertBase(n, base))