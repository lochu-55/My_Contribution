import pytest

@pytest.fixture(params=[(3,4),[3,5]],ids=['tuple','list'])
def fixture01(request):
    return request.param

def test_fix_param01(fixture01):
    assert type(fixture01) in [tuple,list]