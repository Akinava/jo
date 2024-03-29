# -*- coding: utf-8 -*-
import json


__author__ = 'Akinava'
__author_email__ = 'akinava@gmail.com'
__copyright__ = "Copyright © 2019"
__license__ = "MIT License"
__version__ = [0, 0]


class NotFound:
    def __str__(self):
        return 'NOT_FIND'

    def __unicode__(self):
        return 'NOT_FIND'

    def __repr__(self):
        return 'NOT_FIND'

    def __getattr__(self, attr):
        return self

    def __getitem__(self, item):
        return self

    def __call__(self):
        return self

    def __eq__(self, inst):
        return self is inst


not_found = NotFound()


class JO:
    def __init__(self, data=not_found):
        self.__dict__['__data'] = data

    def __getattr__(self, attr):
        return self.__get_data_by_key(attr)

    def __getitem__(self, item):
        return self.__get_data_by_key(item)

    def __setattr__(self, attr, value):
        self.__set_data_by_key(attr, value)
        self._callback_parent()

    def __setitem__(self, item, value):
        self.__set_data_by_key(item, value)
        self._callback_parent()

    def __eq__(self, item):
        return self.__dict__['__data'] == item

    def __str__(self):
        if self.__dict__['__data'] is not_found:
            return 'NOT_FOUND'
        return json.dumps(self.__dict__['__data'], indent=2)

    def __unicode__(self):
        return json.dumps(self.__dict__['__data'], indent=2)

    def __repr__(self):
        if self.__dict__['__data'] is not_found:
            return not_found
        return json.dumps(self.__dict__['__data'])

    def __call__(self, arg):
        self.__dict__['__data'] = arg
        self._callback_parent()

    def __set_data_by_key(self, key, value):
        if not self.__check_data_format_is_dict() and \
           not (self.__check_data_format_is_list() and \
                self.__check_key_is_int(key) and \
                self.__check_key_in_data(key)):
            self.__dict__['__data'] = {}
        self.__dict__['__data'][key] = value

    def __get_data_by_key(self, key):
        if self.__check_data_key(key) is not_found:
            obj = JO()
            obj._set_parent({'item': self, 'key': key})
        else:
            data = self.__dict__['__data'][key]
            obj = JO(data)
        obj._set_parent({'item': self, 'key': key})
        return obj

    def __check_data_key(self, key):
        if self.__check_data_format_is_dict() and self.__check_key_in_data(key) or \
           self.__check_data_format_is_list() and self.__check_key_is_int(key) and self.__check_key_len_for_data(key):
            return
        return not_found

    def __check_data_format_is_dict(self):
        return isinstance(self.__dict__['__data'], dict)

    def __check_data_format_is_list(self):
        return isinstance(self.__dict__['__data'], (list, tuple))

    def __check_key_is_int(self, key):
        return isinstance(key, int)

    def __check_key_len_for_data(self, key):
        return len(self.__dict__['__data']) > key

    def __check_key_in_data(self, key):
        return key in self.__dict__['__data'].keys()

    def _callback_parent(self):
        if not '__parent' in self.__dict__:
            return
        parent = self.__dict__['__parent']
        item = parent['item']
        key = parent['key']
        if item.__dict__['__data'] is not_found or \
           not isinstance(item.__dict__['__data'], dict):
            item.__dict__['__data'] = {}
        item.__dict__['__data'][key] = self._data
        item._callback_parent()

    def _set_parent(self, parent):
        self.__dict__['__parent'] = parent

    def _append(self, value):
        if not isinstance(self.__dict__['__data'], list):
            return False
        self.__dict__['__data'].append(value)
        self._callback_parent()
        return True

    def _has(self, value):
        if isinstance(self.__dict__['__data'], (dict, list)) and value in self.__dict__['__data']:
            return True
        if self.__dict__['__data'] == value:
            return True
        return False

    def _has_value(self, value):
        if isinstance(self.__dict__['__data'], (dict)):
            if value in self.__dict__['__data'].values():
                return True
            else:
                return False
        return self._has(value)

    def _replace(self, from_, to_):
        if self.__check_data_format_is_dict() and from_ in self.__dict__['__data']:
            value = self.__dict__['__data'][from_]
            del self.__dict__['__data'][from_]
            self.__dict__['__data'][to_] = value
            return True
        if self.__check_data_format_is_list() and from_ in self.__dict__['__data']:
            while from_ in self.__dict__['__data']:
                index = self.__dict__['__data'].index(from_)
                self.__dict__['__data'][index] = to_
            return True
        if self.__dict__['__data'] == from_:
            self.__dict__['__data'] == to_
            return True
        return False

    @property
    def _data(self):
        return self.__dict__['__data']

    @property
    def _len(self):
        if self.__check_data_format_is_dict() or \
           self.__check_data_format_is_list():
            return len(self.__dict__['__data'])
        if self.__dict__['__data'] == not_found:
            return not_found
        return None

    @property
    def _type(self):
        if self.__dict__['__data'] == not_found:
            return not_found
        return type(self.__dict__['__data'])
