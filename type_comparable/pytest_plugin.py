import pytest
from _pytest.assertion.util import assertrepr_compare

from type_comparable import TypeComparableDict


@pytest.hookimpl(tryfirst=True)
def pytest_assertrepr_compare(config, op, left, right):
    if op != '==':
        return

    if isinstance(left, TypeComparableDict):
        left = left.data

    if isinstance(right, TypeComparableDict):
        right = right.data

    return assertrepr_compare(config, op=op, left=left, right=right)
