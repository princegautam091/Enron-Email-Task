from functools import wraps
import timeit


def calculate_time(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = timeit.timeit()
        result = f(*args, **kwargs)
        end = timeit.timeit()
        print('Elapsed time: {}'.format(end-start))
        return result
    return wrapper


@calculate_time
def show(n):
    r = []
    for i in range(1, n):
        r.append(i*5)
    return r


# print(show(5))
