import doctest
from doctest import run_docstring_examples
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


def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    if n == 0:
        return k == 0
    while n != 0:
        digit = n % 10
        n = n // 10
        if digit == k: return True
    return False
# run_docstring_examples(has_digit, globals(),True)

def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    cnt = 0
    for num in range(0,10):
        if has_digit(n, num):
            cnt += 1
    return cnt
# run_docstring_examples(unique_digits, globals(),True)
# doctest.testmod(verbose=True)
def repeating(t, n):
    """Return whether t digits repeat to form positive integer n.

    >>> repeating(1, 6161)
    False
    >>> repeating(2, 6161)  # repeats 61 (2 digits)
    True
    >>> repeating(3, 6161)
    False
    >>> repeating(4, 6161)  # repeats 6161 (4 digits)
    True
    >>> repeating(5, 6161)  # there are only 4 digits
    False
    """
    if pow(10, t-1) > n:  # make sure n has at least t digits
        return False
    end = n % pow(10, t)
    rest = n
    while rest:
        if rest % pow(10, t) != end:
           return False
        rest = rest // pow (10, t)
    return True
doctest.testmod(verbose=True)