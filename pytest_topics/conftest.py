import pytest
import os


QA_config = 'qa.prop'
prod_config = 'prod.prop'

def pytest_addoption(parser):
    parser.addoption("--cmdopt",default="QA")

@pytest.fixture()
def CmdOpt(pytestconfig):
    print("\n in c,dopt fixture function..")
    opt = pytestconfig.getoption("cmdopt")

    if opt == 'prod':
        f = open(os.path.join(os.path.dirname(__file__).prod_config), 'r')
    else:
        f = open(os.path.join(os.path.dirname(__file__).QA_config), 'r')

    yield f