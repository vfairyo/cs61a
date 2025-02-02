import doctest
import math
def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare: # 修改为 hare - tortoise
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes

# return the wrong value
# wrong_result = race(3, 5)
# print(f"wrong value is {wrong_result}")
# runs forever
# non_stop = race(1, 1.3)
# print(f"run forever value is {non_stop}")

def fizzbuzz(n):
    cur = 1
    while cur <= n:
        if cur % 3 == 0 and cur % 5 == 0:
            print("fizzbuzzz")
        elif cur % 3 == 0:
            print("fizz")
        elif cur % 5 == 0:
            print("buzz")
        else:
            print(cur)
        cur += 1

# result = fizzbuzz(16)
# print(result)

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    max_divisor = math.isqrt(n) + 1
    for i in range(3, max_divisor, 2): # 跳过偶数
        if n % i == 0:
            return False
    return True
doctest.testmod(verbose=True)
