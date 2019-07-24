#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jo


if __name__ == "__main__":
    '''
    obj = jo.JO({})
    obj.a.b = 1
    print('test 1 1', obj == {'a': {'b': 1}})
    obj.a.b.c = 1
    print('test 1 2', obj == {'a': {'b': {'c': 1}}})

    obj.a.b(1)
    print('test 1 1', obj == {'a': {'b': 1}})
    obj.a.b.c(1)
    print('test 1 2', obj == {'a': {'b': {'c': 1}}})

    obj = jo.JO({})
    obj.a.b.c = 1          # {'a': {'b': {'c': 1}}}
    obj.a.b.d(2)           # {'a': {'b': {'d': 2, 'c': 1}}}
    print('test 2', obj == {'a': {'b': {'d': 2, 'c': 1}}})

    obj = jo.JO({})
    obj.a.b.c = 1
    print('test 3 1', obj == {'a': {'b': {'c': 1}}})
    obj.a.b.c = 2
    print('test 3 2', obj == {'a': {'b': {'c': 2}}})
    obj.a.b.c(3)
    print('test 3 3', obj == {'a': {'b': {'c': 3}}})

    obj = jo.JO()
    obj['a']['b']['c'] = 1
    print(obj == {'a': {'b': {'c': 1}}})

    obj = jo.JO({'a': {'b': {'c': 1}}})
    obj['a'][1] = []
    print(obj == {'a': {1: [], 'b': {'c': 1}}})

    obj = jo.JO({'a': {1: [], 'b': {'c': 1}}})
    obj['a'][7] = {}       # {'a': {1: [], 7: {}}}
    print(obj == {'a': {1: [], 7: {}, 'b': {'c': 1}}})

    '''
    # get
    obj = jo.JO({'a': {1: [1, 2], 'b': {'c': 1}}})
    #print(obj.a[1] == [1, 2])
    #print(obj.a[1][0] == 1)
    #print(obj.a['b'].c == 1)
    print(obj.d is jo.not_found)
    print(obj['d'])
    '''

    # append
    obj = jo.JO({'a': {1: [], 7: {}, 'b': {'c': 1}}})
    res = obj['a'][1]._append(0)  # {'a': {1: [0], 7: {}}}
    print(obj == {'a': {1: [0], 7: {}, 'b': {'c': 1}}})
    print(res is True)
    obj = jo.JO({'a': {1: [], 7: {}, 'b': {'c': 1}}})
    res = obj.b['c']._append(0)
    print(obj == {'a': {1: [], 7: {}, 'b': {'c': 1}}})
    print(res is False)
    '''



    '''
    # has
    obj = jo.JO({1: {1: 1, 2: 2}, 2: 2})
    print(obj[1]._has(1) is True)
    print(obj._has('ololo') is False)

    obj = jo.JO({'a': [1, 2, 'v'], 'b': 2})
    print(obj.a._has('v') is True)
    print(obj.a._has(10) is False)

    obj = jo.JO({'a': 'v', 'b': 2})
    print(obj.a._has_value('v') is True)
    print(obj.a._has_value('a') is False)

    # change
    obj = jo.JO([1, 5, 3, 4, 5])
    res = obj._change(5, 7)
    print(obj == [1, 7, 3, 4, 7])
    print(res is True)

    obj = jo.JO({5: 1, 7: 0})
    res = obj._change(5, 7)
    print(obj == {7: 1})
    print(res is True)

    obj = jo.JO({5: 1, 7: 0})
    res = obj._change(5, 9)
    print(obj == {9: 1, 7: 0})
    print(res is True)

    obj = jo.JO({5: 1, 7: 0})
    res = obj._change_value(1, [1, 2])
    print(obj == {5: [1, 2], 7: 0})
    print(res is True)
    '''



