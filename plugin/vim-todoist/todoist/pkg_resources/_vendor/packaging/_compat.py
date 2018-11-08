# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.


import sys


PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

# flake8: noqa

if PY3:
    string_types = str,
else:
    string_types = str,


def with_metaclass(meta, *bases):
    """
    Create a base class with a metaclass.
    """
    # This requires a bit of explanation: the basic idea is to make a dummy
    # metaclass for one level of class instantiation that replaces itself with
    # the actual metaclass.
    class metaclass(meta):
        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)
    return type.__new__(metaclass, 'temporary_class', (), {})
