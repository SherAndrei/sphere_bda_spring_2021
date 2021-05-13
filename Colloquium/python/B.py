from functools import wraps


def retry(check, n_attempts=5):
    if n_attempts is not None and n_attempts < 1:
        n_attempts = None

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            i = 0
            while not n_attempts or i < n_attempts:
                ans = func(*args, **kwargs)
                if check(ans):
                    return ans
                i += 1
            raise RuntimeError('Expired number of retries')
        return wrapper
    return decorator
