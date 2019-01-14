#!/usr/bin/env python3

'''
init module;

this module defines variables used in other modules;
'''

from collections import Counter
import threading

##  keyed unique values;
_unique_ids = Counter()

##  lock for `_unique_ids`;
_unique_ids_lock = threading.Lock()

