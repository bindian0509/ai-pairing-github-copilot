from functools import lru_cache

FIVE_NAMES = ['Lance', 'Linda', 'Larry', 'Lori', 'Lisa'];
FIVE_AGES = [20, 21, 22, 23, 24];

MAP_NAME_TO_AGE = dict(zip(FIVE_NAMES, FIVE_AGES));

print(MAP_NAME_TO_AGE);


def avg_age():
    return sum(MAP_NAME_TO_AGE.values()) / len(MAP_NAME_TO_AGE);

print(avg_age());


def fib(n):
    if n <= 1:
        return n;
    else:
        return fib(n - 1) + fib(n - 2);

print(fib(10));

@lru_cache(maxsize=None)
def fib_cached(n):
    if n <= 1:
        return n;
    else:
        return fib_cached(n - 1) + fib_cached(n - 2);

print(fib_cached(15));
