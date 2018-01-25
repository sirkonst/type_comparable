About
=====

Module allows to compare variables not only by value but by type too. 

Quick example:

```python
from typing import Any

from type_comparable import make_type_comparable

>> responce = {
    'id': 144233,
    'date_create': '2020-01-25T17:31:33.910803',
    'important_data': 'important data',
    'other_data': 'other data',
}
>> assert make_type_comparable(responce) == {
    'id': int,  # <-- will compare by type int
    'date_create': str, # < -- will compare by type str
    'important_data': 'important data',  # <-- exact match as is
    'other_data': Any, # <-- allow any data
}
```

Very useful for tests by pytest.


Support types
=============

Comparable types (which can be passed to `make_type_comparable()`):
* `int`
* `bool`
* `str`
* `list`
* `dict`

Types for comparison:
* all python builtin (`int`, `str`, `bool`, `list`, `dict`, etc.)
* `object` and `typing.Any` - mean any type

Also you can try to use with your custom types but without guaranteed (verify 
manually before use in product)


Install
=======

From PyPi:

    $ pip install type_comparable


From local:

    $ make install


Development
===========

Prepare and activate virtual enviroment like:

    $ python3 -m venv .env
    # for bash
    source .env/bin/activate
    # for fish
    . .env/bin/activate.fish


Install:

    make install_dev


Run tests:

    make test
