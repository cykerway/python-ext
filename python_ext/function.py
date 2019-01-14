#!/usr/bin/env python3

'''
function module;
'''

import time

from python_ext import _unique_ids
from python_ext import _unique_ids_lock

def clamp(val, min_val=None, max_val=None):

    '''
    clamp a value into range;

    ##  params

    val:

    :   value to clamp;

    min_val:

    :   lower bound (inclusive);

    max_val:

    :   upper bound (inclusive);

    ##  return

    :

    :   clamped value;
    '''

    if max_val is not None:
        val = min(max_val, val)
    if min_val is not None:
        val = max(min_val, val)
    return val

def now():

    '''
    get current time in seconds;
    '''

    return time.time()

def unique_id(key=None):

    '''
    generate a globally unique id on each call; randomness is not guaranteed;

    this function is thread-safe; different threads will not get the same id;

    ##  params

    key:

    :   an arbitrary key for namespacing unique values;

    ##  return

    :

    :   a unique id;
    '''

    with _unique_ids_lock:
        _unique_ids[key] += 1
    return _unique_ids[key]

