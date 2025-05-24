import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} ran in {end_time - start_time:.2f} seconds")
        return result

    return wrapper


@timer
def slow_function():
    sums = 0
    # time.sleep(2)
    for i in range(1, 1_000_000_000):
        sums+=i
    print(sums)


slow_function()
