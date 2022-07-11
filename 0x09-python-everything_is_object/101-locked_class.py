#!/usr/bin/python3
class LockedClass(object):
    def __setattr__(self, key, val):
        if key != "first_name":
            raise AttributeError(
                     "'LockedClass' object has no attribute %r" % key)
        object.__setattr__(self, key, val)
