from functools import partial
from inspect import signature
from shutil import rmtree
from functools import partial, update_wrapper

def wrapped_partial(func, *args, **kwargs):
    partial_func = partial(func, *args, **kwargs)
    update_wrapper(partial_func, func)
    return partial_func


TRUE = 'true'
FALSE = 'false'
NULL = 'null'
