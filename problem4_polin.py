__author__ = 'Sundar'

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
def pol():
    highest=0
    for i in xrange(99999,9999,-1):
        for j in xrange(i,9999,-1):
            poli=str(i*j)
            intpoli=int(poli)
            if poli == poli[::-1] and highest<intpoli :
                highest=intpoli
            elif intpoli < highest:
                break

    return highest
print pol()
