import functools
import signal as sig
from time import sleep


class TimeoutException(RuntimeError):
    def __init__(self, message=None):
        super().__init__(message)


def timeout(seconds=0.5):
    def decorator(func):
        if not seconds or seconds <= 0.:
            return func

        def handler(signum, frame):
            raise TimeoutException("Timed out")

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            prev = sig.signal(sig.SIGALRM, handler)
            sig.setitimer(sig.ITIMER_REAL, seconds)
            try:
                return func(*args, **kwargs)
            finally:
                sig.setitimer(sig.ITIMER_REAL, 0)
                sig.signal(sig.SIGALRM, prev)
        return wrapper
    return decorator
