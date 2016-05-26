#https://projecteuler.net/problem=2

fibs = {
    1:1,
    2:2
}

def fibo(n):
    if n in fibs:
        return fibs[n]
    else:
        i = 3
        while (i < n + 1):
            fibs[i] = fibs[i - 1] + fibs[i - 2]
            i = i + 1
        return fibs[n]

even_fibs_sum = 0
latest_fibs = 0
i = 1

while(True):
    print(i)
    if latest_fibs >= 4000000: break
    f = fibo (i)
    if f % 2 == 0 :
        print('fibo is ' + str(f))
        even_fibs_sum = even_fibs_sum + f
        print('sum is ' + str(even_fibs_sum))
    latest_fibs = f
    i += 1

print(even_fibs_sum)
