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
    print sum(i for i in xrange(1,1000) if i % 3 == 0 or i % 5 == 0)



if __name__ == '__main__':
    main()
