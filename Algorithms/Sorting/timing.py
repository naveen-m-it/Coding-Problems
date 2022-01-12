import time
def timed_func(func_to_time):
    def timed(*args,**kwargs):
        start = time.perf_counter()
        res = func_to_time(*args,**kwargs)
        t = time.perf_counter()-start
        print("[Finished in %.3fs]"%t)
        return res
    return timed