import pytest


def pytest_configure():
    pytest.wk1 = ["mon","tue","wed"]
    pytest.wk2 = ["fri","sat","sun"]

@pytest.fixture(scope="module")
def setup01():
    wk = pytest.wk1.copy()
    wk.append("thu")
    yield wk
    print("\n fixture01 is closing....")

@pytest.fixture(scope="session")
def setup02():
    w2=pytest.wk2.copy()
    w2.insert(0,"thu")
    yield w2
    print("\n fixture02 is closing...")


@pytest.fixture()
def setup04(request):
    mon = getattr(request.module,"month")
    print("\n in fixture setup04")
    print("\n fixture scope : "+str(request.scope))
    print("\n calling function:..."+str(request.function.__name__))
    print("\n calling function..:"+str(request.function.__name__))
    mon.append("april")
    yield mon


@pytest.fixture()
def setup05():
    def get_struct(name):
        if name == "list":
            return [1,2,3]
        elif name == "tuple":
            return (1,2,4)
    return get_struct

