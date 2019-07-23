# -*- coding: utf-8 -*-
import json


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


not_find = NotFound()


class JO:
    def __init__(self, data):
        self.__dict__['__data'] = data

    def __getattr__(self, attr):
        return self.__get_data_by_key(attr)

    def __getitem__(self, item):
        return self.__get_data_by_key(item)

    def __setattr__(self, attr, value):
        self.__set_data_by_key(attr, value)

    def __setitem__(self, item, value):
        self.__set_data_by_key(item, value)

    def __eq__(self, item):
        return self.__dict__['__data'] == item

    def __str__(self):
        return json.dumps(self.__dict__['__data'], indent=2)

    def __unicode__(self):
        return json.dumps(self.__dict__['__data'], indent=2)

    def __repr__(self):
        return json.dumps(self.__dict__['__data'], indent=2)

    def __call__(self, *args, **kwargs):
        return not_find

    def __set_data_by_key(self, key, value):
        if not self.__check_data_format_is_dict() and \
           not (self.__check_data_format_is_list() and \
                self.__check_key_is_int(key) and \
                self.__check_key_in_data(key)):
            self.__dict__['__data'] = {}
        self.__dict__['__data'][key] = value

    def __get_data_by_key(self, key):
        if self.__check_data_key(key) is not_find:
            return not_find
        data = self.__dict__['__data'][key]
        return BDATA(data)

    def __check_data_key(self, key):
        if self.__check_data_format_is_dict() and self.__check_key_in_data(key) or \
           self.__check_data_format_is_list() and self.__check_key_is_int(key) and self.__check_key_len_for_data(key):
            return
        return not_find

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

    @property
    def _data(self):
        return self.__dict__['__data']


