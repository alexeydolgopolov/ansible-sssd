#!/usr/bin/env python

from functools import reduce

class FilterModule(object):
    def filters(self):
        return {
            'longoptions': lambda list: reduce(lambda x, y: x + " --" + y, list, '')
        }
