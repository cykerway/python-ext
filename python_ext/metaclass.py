#!/usr/bin/env python3

'''
metaclass module;
'''

class Singleton(type):

    '''
    this is a metaclass to help make a class a singleton;

    for example, to make class `Foo` a singleton, declare it as:

        class Foo(metaclasssss=Singleton)

    with this declaration, trying to create multiple instances will raise;
    '''

    ##  dict: (classes) > (singleton instances);
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self in self._instances:
            raise Exception('singleton exists: {!r}'.format(self))
        self._instances[self] = super().__call__(*args, **kwargs)
        return self._instances[self]

