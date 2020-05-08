import functools
import time

#------------------------Start of do_twice()-----------------------
#Current iteration (4) of do_twice
def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

#Iteration 1 of do_twice:
def do_twice_it_1(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

#Iteration 2 of do_twice:
def do_twice_it_2(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

#Iteration 3 of do_twice:
def do_twice_it_3(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

#------------------------End of do_twice()--------------------------

#------------------------Start of decorator()-----------------------
#Current iteration (1) of decorator:
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

#------------------------End of decorator()--------------------------

#------------------------Start of timer()----------------------------
#Current iteration (1) of timer:
def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer
#------------------------End of timer()------------------------------

#------------------------Start of debug()----------------------------
#Current iteration (1) of debug:
def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug
#------------------------End of debug()------------------------------

#------------------------Start of slow_down()----------------------------
#Current iteration (1) of slow_down:
def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down
#------------------------End of slow_down()----------------------------
