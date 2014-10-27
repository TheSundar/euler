
import cProfile
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
    a = 1
    b = 2
    total = 0
    while a < 4000000:
        a, b = b, a + b
        if a % 2 == 0:
            total += a
    print total


if __name__ == '__main__':
    main()
