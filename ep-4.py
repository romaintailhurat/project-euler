#https://projecteuler.net/problem=4

def hasEvenLen(n):
    return len(str(n)) % 2 == 0

def isPalindrome(n):
    if hasEvenLen(n):
        return isPalindromeEven(n)
    else:
        return isPalindromeOdd(n)

def isPalindromeEven(n):
    s = str(n)
    first_half = s[0:len(s)/2]
    second_half = s[len(s)/2:len(s)]
    return first_half == second_half[::-1]

def isPalindromeOdd(n):
    s = str(n)
    first_half = s[0:len(s)/2]
    second_half = s[len(s)/2+1:len(s)]
    return first_half == second_half[::-1]

palindrome = 0

limit = 1000

for i in range(limit):
    for j in range(limit):
        prod = i * j
        if isPalindrome(prod) and prod > palindrome:
            palindrome = prod

print(palindrome)
