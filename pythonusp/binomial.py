from math import factorial


def binomial(n, k):
    nfatorial = factorial(n)
    kfatorial = factorial(k)
    bin = nfatorial/(kfatorial*factorial((n - k)))
    return bin


n = 5
k = 3
print(binomial(n, k))
