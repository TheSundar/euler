import math
import cProfile


def is_prime(n):
    if n <= 1:
        return False
    elif n % 2 == 0 and n != 2:
        return False
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def do_cprofile(func):
    def profiled_func(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:
            profile.print_stats()

    return profiled_func


@do_cprofile
def main():
    num = 600851475143
    number = int(math.sqrt(600851475143)) + 1
    for i in xrange(1, number):
        if num % i == 0 and is_prime(i):
            print i


if __name__ == '__main__':
    main()
