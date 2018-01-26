About
=====

Module allows to compare variables not only by value but by type too. 

Quick example:

```python
from typing import Any

from type_comparable import make_type_comparable

>> response = {
    'id': 144233,
    'date_create': '2020-01-25T17:31:33.910803',
    'important_data': 'important data',
    'other_data': 'other data',
}
>> assert make_type_comparable(response) == {
    'id': int,  # <-- will compare by type int
    'date_create': str, # < -- will compare by type str
    'important_data': 'important data',  # <-- exact match as is
    'other_data': Any, # <-- allow any data
}

# if you don't want wrap left variable (response) if can wrap right:
>> assert response == make_type_comparable(...)
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
* `object` and `typing.Any` - mean any type but not `None`
* `typing.Optional` - mean any type and `None`. `Optional[int]` now not supported

Also you can try to use with your custom types but without guaranteed (verify 
manually before use in product)


Know issues
===========

Wrapper `None` is not `None` :-(

```python
>> make_type_comparable(None) is None
False

# use equal
>> make_type_comparable(None) == None
True
```


Install
=======

From PyPi:

    $ pip install type_comparable


From local:

    # update setuptools
    $ pip install 'setuptools >= 30.4'
    # do install
    $ make install
    # or
    $ pip install .


Development
===========

Prepare and activate virtual enviroment like:

    $ python3 -m venv .env
    # for bash
    source .env/bin/activate
    # for fish
    . .env/bin/activate.fish
    
Update pre-install dependencies:

    $ pip install 'setuptools >= 30.4'


Install:

    $ make install_dev
    # or
    $ pip install --editable .[develop]

Run tests:

    $make test
    # or 
    $ pytest tests/
