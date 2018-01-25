from collections import UserDict, UserList
from sys import maxsize
from typing import Any

import pytest

from type_comparable import make_type_comparable


int_comparable_types = [int, object, Any]
str_comparable_types = [str, object, Any]
bool_comparable_types = [bool, object, Any]
list_comparable_types = [list, object, Any]
dict_comparable_types = [dict, object, Any]


class TestSimple:

    def test_none(self):
        obj = make_type_comparable(None)
        assert obj == None

    @pytest.mark.parametrize('value', [0, 1, -1, maxsize, -maxsize])
    @pytest.mark.parametrize('compare_with', int_comparable_types)
    def test_int(self, value, compare_with):
        assert value != compare_with

        obj = make_type_comparable(value)
        assert isinstance(obj, int)
        assert obj == value
        assert obj == compare_with
        assert obj != value + 1
        assert obj != None

    @pytest.mark.parametrize('value', [True, False])
    @pytest.mark.parametrize('compare_with', bool_comparable_types)
    def test_bool(self, value, compare_with):
        assert value != compare_with

        obj = make_type_comparable(value)
        assert isinstance(obj, bool)
        assert obj == value
        assert obj == compare_with
        assert obj != (not value)
        assert obj != None

    @pytest.mark.parametrize('value', ['', 'a', 'aaaaaaaaaaaaaaaaaaaaaaaaaaa'])
    @pytest.mark.parametrize('compare_with', str_comparable_types)
    def test_str(self, value, compare_with):
        assert value != compare_with

        obj = make_type_comparable(value)
        assert isinstance(obj, str)
        assert obj == value
        assert obj == compare_with
        assert obj != '{}-other'.format(value)
        assert obj != None

    @pytest.mark.parametrize('value', [[], [1, ], [1, 2, 3]])
    @pytest.mark.parametrize('compare_with', list_comparable_types)
    def test_list(self, value, compare_with):
        assert value != compare_with

        obj = make_type_comparable(value)
        assert isinstance(obj, UserList)
        assert obj == value
        assert obj == compare_with
        assert obj != [*value, 0]
        assert obj != None

    @pytest.mark.parametrize('value', [{}, {'a': 'A'}])
    @pytest.mark.parametrize('compare_with', dict_comparable_types)
    def test_dict(self, value, compare_with):
        assert value != compare_with

        obj = make_type_comparable(value)
        assert isinstance(obj, UserDict)
        assert obj == value
        assert obj == compare_with
        assert obj != {**value, 'other_key': 'other_value'}
        assert obj != None


class TestDictValues:

    @staticmethod
    def make_simple_dict():
        return {
            'int': 1,
            'str': 'value str',
            'bool': True,
            'none': None,
            'dict': {},
            'list': [],
            'additional key': 'additional value'
        }

    @classmethod
    def make_complex_dict(cls):
        d = cls.make_simple_dict()
        d['dict'] = cls.make_simple_dict()
        return d

    @pytest.mark.parametrize('field_int', int_comparable_types)
    @pytest.mark.parametrize('field_str', str_comparable_types)
    @pytest.mark.parametrize('field_bool', bool_comparable_types)
    @pytest.mark.parametrize('field_dict', dict_comparable_types)
    @pytest.mark.parametrize('field_list', list_comparable_types)
    def test_values(
        self, field_int, field_str, field_bool, field_dict, field_list
    ):
        dct = self.make_simple_dict()
        expect = self.make_simple_dict()
        expect['int'] = field_int
        expect['str'] = field_str
        expect['bool'] = field_bool
        expect['dict'] = field_dict
        expect['list'] = field_list

        assert dct != expect

        obj = make_type_comparable(dct)
        assert isinstance(obj, UserDict)
        assert obj == expect
        assert obj['int'] == field_int
        assert obj['str'] == field_str
        assert obj['bool'] == field_bool
        assert obj['dict'] == field_dict
        assert obj['list'] == field_list
        assert obj != {**expect, 'additional key': 'changed'}
        assert obj != {**expect, 'new key': 'new value'}

    @pytest.mark.parametrize('field_int', int_comparable_types)
    @pytest.mark.parametrize('field_str', str_comparable_types)
    @pytest.mark.parametrize('field_bool', bool_comparable_types)
    @pytest.mark.parametrize('field_dict', dict_comparable_types)
    @pytest.mark.parametrize('field_list', list_comparable_types)
    def test_sub_dict_values(
        self, field_int, field_str, field_bool, field_dict, field_list
    ):
        dct = self.make_complex_dict()
        expect = self.make_complex_dict()
        expect['dict']['int'] = field_int
        expect['dict']['str'] = field_str
        expect['dict']['bool'] = field_bool
        expect['dict']['dict'] = field_dict
        expect['dict']['list'] = field_list

        assert dct != expect

        obj = make_type_comparable(dct)
        assert isinstance(obj, UserDict)
        assert obj == expect
        assert obj['dict']['int'] == field_int
        assert obj['dict']['str'] == field_str
        assert obj['dict']['bool'] == field_bool
        assert obj['dict']['dict'] == field_dict
        assert obj['dict']['list'] == field_list
        assert obj != {**expect, 'additional key': 'changed'}
        assert obj != {**expect, 'new key': 'new value'}


class TestListValues:

    @staticmethod
    def make_simple_list():
        return [1, 'value str', True, None, {}, [], 'additional value']

    @classmethod
    def make_complex_list(cls):
        l = cls.make_simple_list()
        l.append(cls.make_simple_list())
        return l

    @pytest.mark.parametrize('field_int', int_comparable_types)
    @pytest.mark.parametrize('field_str', str_comparable_types)
    @pytest.mark.parametrize('field_bool', bool_comparable_types)
    @pytest.mark.parametrize('field_dict', dict_comparable_types)
    @pytest.mark.parametrize('field_list', list_comparable_types)
    def test_values(
        self, field_int, field_str, field_bool, field_dict, field_list
    ):
        dct = self.make_simple_list()
        expect = self.make_simple_list()
        expect[0] = field_int
        expect[1] = field_str
        expect[2] = field_bool
        expect[4] = field_dict
        expect[5] = field_list

        assert dct != expect

        obj = make_type_comparable(dct)
        assert isinstance(obj, UserList)
        assert obj == expect
        assert obj[0] == field_int
        assert obj[1] == field_str
        assert obj[2] == field_bool
        assert obj[4] == field_dict
        assert obj[5] == field_list
        _expect = [*expect]
        _expect[6] = 'changed'
        assert obj != _expect
        assert obj != [*expect, 'new value']

    @pytest.mark.parametrize('field_int', int_comparable_types)
    @pytest.mark.parametrize('field_str', str_comparable_types)
    @pytest.mark.parametrize('field_bool', bool_comparable_types)
    @pytest.mark.parametrize('field_dict', dict_comparable_types)
    @pytest.mark.parametrize('field_list', list_comparable_types)
    def test_inner_list_values(
        self, field_int, field_str, field_bool, field_dict, field_list
    ):
        dct = self.make_complex_list()
        expect = self.make_complex_list()
        expect[7][0] = field_int
        expect[7][1] = field_str
        expect[7][2] = field_bool
        expect[7][4] = field_dict
        expect[7][5] = field_list

        assert dct != expect

        obj = make_type_comparable(dct)
        assert isinstance(obj, UserList)
        assert obj == expect
        assert obj[7][0] == field_int
        assert obj[7][1] == field_str
        assert obj[7][2] == field_bool
        assert obj[7][4] == field_dict
        assert obj[7][5] == field_list
        _expect = [*expect]
        _expect[7][6] = 'changed'
        assert obj != _expect
        assert obj != [*expect, 'new value']


def test_pytest():

    assert {'a': 'A', 'b': 'B'} == make_type_comparable({'a': 'A', 'b': 'b'})