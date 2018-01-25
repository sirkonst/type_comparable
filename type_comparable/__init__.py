from collections import UserDict, UserList
from typing import Any

from wrapt import ObjectProxy

__all__ = 'make_type_comparable', 'TypeComparableObject'


class TypeComparableObject:

    def __eq__(self, other):
        if other is Any:
            return True

        if isinstance(other, type):
            return isinstance(self, other)

        return super().__eq__(other)


class TypeComparableDict(TypeComparableObject, UserDict):

    def __eq__(self, other):
        if other is dict:
            return True

        return super().__eq__(other)

    def __getitem__(self, item):
        obj = super().__getitem__(item)

        return make_type_comparable(obj)


class TypeComparableList(TypeComparableObject, UserList):

    def __eq__(self, other):
        if other is list:
            return True

        if self.data == other:
            return True

        if super().__eq__(other):
            return True

        wrapped_data = [make_type_comparable(obj) for obj in self.data]
        return wrapped_data == other

    def __getitem__(self, index):
        obj = super().__getitem__(index)

        return make_type_comparable(obj)


__cache = {}


def make_type_comparable(obj):
    if obj is None:
        return obj
    elif isinstance(obj, TypeComparableObject):
        return obj
    elif isinstance(obj, dict):
        wrapper_cls = TypeComparableDict
    elif isinstance(obj, list):
        wrapper_cls = TypeComparableList
    else:
        cls = type(obj)
        wrapper_name = 'TypeComparable[{}]'.format(cls.__name__)
        cache_key = id(cls)
        if cls is bool:
            cls = ObjectProxy

        wrapper_cls = __cache.get(cache_key)
        if not wrapper_cls:
            wrapper_cls = type(
                wrapper_name, (TypeComparableObject, cls), {}
            )
            __cache[cache_key] = wrapper_cls

    return wrapper_cls(obj)
