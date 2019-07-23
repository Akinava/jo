#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jo


if __name__ == "__main__":
    obj = jo.JO({})
    # set
    #obj.a.b = 1
    print(obj)
    obj.a.b.c = 1          # {'a': {'b': {'c': 1}}}
    print(obj)
    #obj.a.b({'d': 2})      # {'a': {'b': {'d': 2}}}
    #obj.a._merge({'o': 7}) # {'a': {'b': {'d':2}, 'o': 7}}
    #obj['a']['b']['c'] = 1 # {'a': {'b': {'d':2}, 'o': 7, 'c': 1}}
    #obj['a'][1] = []       # {'a': {1: []}}
    #obj['a'][7] = {}       # {'a': {1: [], 7: {}}}
    #obj['a'][1].append(0)  # {'a': {1: [0], 7: {}}}
    #obj['a'][1][5] = 1     # Error
    #obj['a'][1][5](1)      # Error
    # get
    #obj['a'].b             # not_find
    #obj.b.a                # not_find
    #obj.a[1][1]            # not_find

