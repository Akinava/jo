# JSON to OBJECT
- intention  
That code helps to manipulate with a [JSON](https://en.wikipedia.org/wiki/JSON) object as a class.

- required  
python3.x


- usage  

attributes can be got two ways  
obj.attr_name  
or  
obj['attr_name']  

set data
```python
>>> import jo
>>> obj = jo.JO()
>>> obj.a.b = 1
>>> obj
{'a': {'b': 1}}
>>> obj = jo.JO()
>>> obj['a']['b']['c'] = 1
obj
{'a': {'b': {'c': 1}}}
```

get data
```python
>>> import jo
>>> obj = jo.JO({'a': {1: [1, 2], 'b': {'c': 1}}})
>>> obj.a[1]
[1, 2]
```

append
```python
>>> import jo
>>> obj = jo.JO({'a': {1: [], 7: {}, 'b': {'c': 1}}})
>>> obj['a'][1]._append(0)
True
>>> obj
{'a': {1: [0], 7: {}, 'b': {'c': 1}}}
```

check attr
```python
>>> import jo
>>> obj = jo.JO({1: {1: 1, 2: 2}, 2: 2})
>>> obj[1]._has(1)
True
```

check dict has value
```python
>>> import jo
>>> obj = jo.JO({'a': 'v', 'b': 2})
>>> obj._has_value('v')
True
```

get length
```python
>>> import jo
>>> obj = jo.JO({})
>>> obj._len
0
```

get type
```python
>>> import jo
>>> obj = jo.JO({})
>>> obj._type
dict
```

replace
```python
>>> import jo
>>> obj = jo.JO([1, 5, 3, 4, 5]) 
>>> res = obj._replace(5, 7)
>>> res
[1, 7, 3, 4, 7] 
```
