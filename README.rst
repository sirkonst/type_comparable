About
=====

Module allows to compare variables not only by value but by type too. 

Quick example:

.. code-block:: python

    from typing import Any

    from type_comparable import make_type_comparable

    response = {
        'id': 144233,
        'date_create': '2020-01-25T17:31:33.910803',
        'important_data': 'important data',
        'other_data': 'other data',
        'inner_data': {
            'field a': 'value a',
            'field d': 'value b'
        },
        'line': [1, 'some text', 3]
    }
    assert make_type_comparable(response) == {
        'id': int,  # <-- will compare by type int
        'date_create': str, # < -- will compare by type str
        'important_data': 'important data',  # <-- exact match as is
        'other_data': Any, # <-- allow any data,
        'inner_date': {  # <-- also work with nested dictionaries
            'field a': str,
            'field b': 'value b'
        }
        'line': [int, Any, 3]  # <- check elements in array
    }

    # if you don't want wrap left variable (response) if can wrap right:
    assert response == make_type_comparable(...)

Very useful for tests by pytest.


Support types
=============

Comparable types (which can be passed to `make_type_comparable()`):
* `int`
* `bool`
* `str`
* `list`
* `dict`
* other

Types for comparison:
* all python builtin (`int`, `str`, `bool`, `list`, `dict`, etc.)
* `object` and `typing.Any` - mean any type but not `None`
* `typing.Optional` - mean any type and `None`. `Optional[int]` now not supported

Also you can try to use with your custom types but without guaranteed (verify 
manually before use in product)


Know issues
===========

Wrapped `None` is not `None` :-(

.. code-block:: python

    >> make_type_comparable(None) is None
    False

    # use equal
    >> make_type_comparable(None) == None
    True


Install
=======

From PyPi:

.. code-block:: bash

    $ pip install type_comparable


From local:

.. code-block:: bash

    # update setuptools
    $ pip install 'setuptools >= 30.4'
    # do install
    $ make install
    # or
    $ pip install .


Development
===========

Prepare and activate virtual environment like:

.. code-block:: bash

    $ python3 -m venv .env
    # for bash
    $ source .env/bin/activate
    # for fish
    $ . .env/bin/activate.fish
    
Update pre-install dependencies:

.. code-block:: bash

    $ pip install 'setuptools >= 30.4'


Install:

.. code-block:: python

    $ make install_dev
    # or
    $ pip install --editable .[develop]

Run tests:

.. code-block:: python

    $ make test
    # or 
    $ pytest tests/
