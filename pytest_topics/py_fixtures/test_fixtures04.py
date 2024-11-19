import pytest

def test_del(setup01):
    del setup01[-1]
    print(setup01)
    assert setup01 == pytest.wk1

def test_remove(setup02):
    print(setup02)
    setup02.remove("thu")
    assert setup02 == pytest.wk2

month = ["jan","feb","mar"]
def test_check(setup04):
    assert "april" in setup04
    assert len(setup04) == 4

def test_fact(setup05):
    assert type(setup05('list')) == list
    assert type(setup05('tuple')) == tuple