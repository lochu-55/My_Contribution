import pytest

wk1 = ["mon","tue","wed"]
wk2 = ["fri","sat","sun"]

@pytest.fixture()
def setup01():
    w1 = wk1.copy()
    w1.append("thu")
    yield w1
    print("after yield...tearing down")
    w1.pop()

def test_extendlist(setup01):
    setup01.extend(wk2)
    assert setup01 == ["mon","tue","wed","thu","fri","sat","sun"]

@pytest.fixture()
def setup02():
    w2 = wk2.copy()
    w2.insert(0,"thu")
    yield w2

def test_len(setup01,setup02):
    assert len(wk1+setup02) == len(setup01+wk2)
    print(len(wk1+wk2))

