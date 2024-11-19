import sys
import pytest


pytestmark = pytest.mark.skipif(sys.platform == 'win32',reason = "will run only on OS ")
c = 9/5
def cent_to_fah(cent = 0):
    fah = (cent*c)+32
    return fah
print(cent_to_fah())


@pytest.mark.skip(reason="skipping for no reason")
def test_c1():
    assert type(c) == float


@pytest.mark.sanity
#@pytest.mark.skipif(cent_to_fah() == 32 ,reason = "skipping for no specified reason")
def test_c2():
    assert cent_to_fah() == 32

@pytest.mark.fast
#@pytest.mark.skipif(sys.version_info < (3,6) ,reason = "python version is less")
def test_c3():
    assert cent_to_fah(38) == 100.4


@pytest.mark.smoke
#@pytest.mark.skipif(pytest.__version__ < '5.5.0' ,reason = "pytest version is less")
def test_c4():
    assert cent_to_fah(38) == 100.4

