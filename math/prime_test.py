'''
prime_test(n) returns a True if n is a prime number else it returns False
'''


def prime_test(n):
    if n <= 1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    j = 3
    while(j*j <= n):
        if n%(j)==0:
            return False
        j += 1
    return True