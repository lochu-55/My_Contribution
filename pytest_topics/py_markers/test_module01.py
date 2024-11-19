import pytest
pytestmark = pytest.mark.external

@pytest.mark.sanity
def test_case01():
    assert 5+4 == 9
    assert 7/7 == 1
    assert 5*3 == 15

@pytest.mark.smoke
def test_case02():
    assert ((3-1)*4/2) == 3


@pytest.mark.external
@pytest.mark.xfail(raises=AssertionError)
def test_case03():
    assert 4//2 == 1