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
def pol(n):
    highest=0
    left=int(str(n)[:-1])
    for i in xrange(n,left,-1):
        if i * n < highest:
            break
        for j in xrange(i,left,-1):
            poli=str(i*j)
            intpoli=int(poli)
            if poli == poli[::-1] and highest<intpoli :
                highest=intpoli
            elif intpoli < highest:
                break

    return highest
print pol(99999)

