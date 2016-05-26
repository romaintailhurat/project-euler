# https://projecteuler.net/problem=1
def is_mod_3_or_5(n):
    if n <= 0 :
        return False
    return n % 3 == 0 or n % 5 == 0

mods = filter(is_mod_3_or_5, range(1,1000))
m_sum = reduce(lambda x,y : x + y, mods)
print(m_sum)
