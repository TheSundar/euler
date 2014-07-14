from Queue import Queue
import threading
import time

t0 = time.time()


def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n /= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac
# queueLock = threading.Lock()
#
# sum1={}
#
# def do_stuff(q):
#     print threading.current_thread()
#     while True:
#
#         x=q.get()
#
#
#         q.task_done()
#
# q = Queue(maxsize=0)
# num_threads = 500
#
# for i in range(num_threads):
#   worker = threading.Thread(target=do_stuff, args=(q,))
#   worker.setDaemon(True)
#   worker.start()
sum1={}
for x in xrange(1,1000000):
    if 3<len(set(primes(x)))<5:

        if len(set(primes(x)))==len(set(primes(x+1)))==len(set(primes(x+2)))==len(set(primes(x+3)))==4:

            if reduce(lambda x,y:x*y,primes(x))+3 ==reduce(lambda x,y:x*y,primes(x+1))+2 == reduce(lambda x,y:x*y,primes(x+2))+1==reduce(lambda x,y:x*y,primes(x+3)):
                print  x,x+1,x+2,x+3





