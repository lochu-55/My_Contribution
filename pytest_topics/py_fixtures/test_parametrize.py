import pytest
import math

data = [
    ([2,3,4],'sum',9),
    ([2,3,4],'prod',24)
]

@pytest.mark.parametrize('test_inp',[82,45,78,67])
def test_para(test_inp):
    assert test_inp > 50


@pytest.mark.parametrize("inp,out",[(2,4),(3,9),(4,16)])
def test_sq(inp,out):
    assert (inp**2) == out


@pytest.mark.parametrize("a,b,c",data)
def test_para01(a,b,c):
    if b == 'sum':
        assert sum(a) == c

    elif b == 'prod':
        assert math.prod(a) == c
