#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jo


if __name__ == "__main__":
    # set
    obj = jo.JO()
    obj.a.b = 1
    print('test set 1', obj == {'a': {'b': 1}})
    obj.a.b.c = 1
    print('test set 2', obj == {'a': {'b': {'c': 1}}})

    obj.a.b(1)
    print('test set 3', obj == {'a': {'b': 1}})
    obj.a.b.c(1)
    print('test set 4', obj == {'a': {'b': {'c': 1}}})

    obj = jo.JO({})
    obj.a.b.c = 1          # {'a': {'b': {'c': 1}}}
    obj.a.b.d(2)           # {'a': {'b': {'d': 2, 'c': 1}}}
    print('test set 5', obj == {'a': {'b': {'d': 2, 'c': 1}}})

    obj = jo.JO({})
    obj.a.b.c = 1
    print('test set 6', obj == {'a': {'b': {'c': 1}}})
    obj.a.b.c = 2
    print('test set 7', obj == {'a': {'b': {'c': 2}}})
    obj.a.b.c(3)
    print('test set 8', obj == {'a': {'b': {'c': 3}}})

    obj = jo.JO()
    obj['a']['b']['c'] = 1
    print('test set 9', obj == {'a': {'b': {'c': 1}}})

    obj = jo.JO({'a': {'b': {'c': 1}}})
    obj['a'][1] = []
    print('test set 10', obj == {'a': {1: [], 'b': {'c': 1}}})

    obj = jo.JO({'a': {1: [], 'b': {'c': 1}}})
    obj['a'][7] = {}
    print('test set 11', obj == {'a': {1: [], 7: {}, 'b': {'c': 1}}})

    # get
    obj = jo.JO({'a': {1: [1, 2], 'b': {'c': 1}}})
    print('test get 1', obj.a[1] == [1, 2])
    print('test get 2', obj.a[1][0] == 1)
    print('test get 3', obj.a['b'].c == 1)
    print('test get 4', obj.d == jo.not_found)

    # append
    obj = jo.JO({'a': {1: [], 7: {}, 'b': {'c': 1}}})
    res = obj['a'][1]._append(0)
    print('test append 1', obj == {'a': {1: [0], 7: {}, 'b': {'c': 1}}})
    print('test append 2', res is True)
    obj = jo.JO({'a': {1: [], 7: {}, 'b': {'c': 1}}})
    res = obj.b['c']._append(0)
    print('test append 3', obj == {'a': {1: [], 7: {}, 'b': {'c': 1}}})
    print('test append 4', res is False)

    # has
    obj = jo.JO({1: {1: 1, 2: 2}, 2: 2})
    print('test has 1', obj[1]._has(1) is True)
    print('test has 2', obj._has('ololo') is False)

    obj = jo.JO({'a': [1, 2, 'v'], 'b': 2})
    print('test has 3', obj.a._has('v') is True)
    print('test has 4', obj.a._has(10) is False)

    obj = jo.JO(100500)
    print('test has 5', obj._has(100500) is True)

    obj = jo.JO({'b': 2})
    print('test has 6', obj.a._has(jo.not_found) is True)

    # has value
    obj = jo.JO({'a': 'v', 'b': 2})
    print('test has value 1', obj.a._has_value('v') is True)
    print('test has value 2', obj.a._has_value('a') is False)

    obj = jo.JO({'a': [1, 2, 'v']})
    print('test has value 3', obj['a']._has_value('v') is True)

    obj = jo.JO(1)
    print('test has value 4', obj._has_value(1) is True)

    # len
    obj = jo.JO([1, 2, 'v'])
    print('test len 1', obj._len == 3)
    obj = jo.JO({})
    print('test len 2', obj._len == 0)
    obj = jo.JO(1)
    print('test len 3', obj._len is None)
    obj = jo.JO('qweqwe')
    print('test len 4', obj._len is None)
    obj = jo.JO()
    print('test len 5', obj._len == jo.not_found)

    # type
    obj = jo.JO([1, 2, 'v'])
    print('test type 1', obj._type == list)
    obj = jo.JO({})
    print('test type 2', obj._type == dict)
    obj = jo.JO(1)
    print('test type 3', obj._type is int)
    obj = jo.JO('qweqwe')
    print('test type 4', obj._type is str)
    obj = jo.JO()
    print('test type 5', obj._type == jo.not_found)

    # replace
    obj = jo.JO([1, 5, 3, 4, 5])
    res = obj._replace(5, 7)
    print('test replace 1', obj == [1, 7, 3, 4, 7])
    print('test replace 2', res is True)

    obj = jo.JO({5: 1, 7: 0})
    res = obj._replace(5, 7)
    print('test replace 3', obj == {7: 1})
    print('test replace 4', res is True)

    obj = jo.JO({5: 1, 7: 0})
    res = obj._replace(5, 9)
    print('test replace 5', obj == {9: 1, 7: 0})
    print('test replace 6', res is True)
