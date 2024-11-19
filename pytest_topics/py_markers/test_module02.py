import pytest

def test_case01():
     with pytest.raises(ZeroDivisionError):
         assert (1/0)

def func1():
    raise ValueError("IndexError of func1 is raised")



def test_case02():
    with pytest.raises(Exception)  as excinfo:
        assert (1,2,3) == (1,2,4)
    print(str(excinfo))

@pytest.mark.smoke
def test_case03():
    with pytest.raises(Exception) as exc:
        func1()
    print(str(exc))
    assert (str(exc.value)) == 'Exception func1 is raised'