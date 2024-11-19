import pytest
import os

filename = 'file.txt'

@pytest.fixture()
def setup03():
    f = open(filename,"w")
    f.write("pytest is good")
    f.close()
    f=open(filename,"r+")
    yield f
    f.close()
    os.remove(filename)

def test_filetest(setup03):
    assert(setup03.readline()) == "pytest is good"
