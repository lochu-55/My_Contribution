import pytest
import sys
pytestmark = [pytest.mark.slow,pytest.mark.fast]


@pytest.mark.smoke
def test_str01():
    n = 9/4
    s1 = "I like "+"pytest automation"
    assert str(n) == '2.25'
    assert s1 == "I like pytest automation"
    assert s1 + str(n) == "I like pytest automation2.25"

@pytest.mark.smoke
def test_str02():
    letter = "abcdefghijklmnopqrstuvwxyz"
    assert len(letter) == 26


@pytest.mark.smoke
@pytest.mark.sanity
def test_strslice():
    letter = "abcdefghijklmnopqrstuvwxyz"
    assert letter[0]=='a'
    assert letter[-1]=='z'
    assert letter[10:] == "klmnopqrstuvwxyz"
    assert letter[-3:] == "xyz"

def test_strsplit():
    s1 = "python,pytest and automation"
    assert s1.split() == ["python,pytest", "and", "automation"]
    assert s1.split(',') == ["python" , "pytest and automation"]

def test_strjoin():
    pass
    s1 = "python,pytest and automation"
    l1 = ["python,pytest", "and", "automation"]
    assert " ".join(l1) == s1

@pytest.mark.xfail( raises= IndexError ,reason = "known issue")
def test_str04():
    letter="abcdefghijklmnopqrstuvwxyz"
    assert letter[100]

@pytest.mark.xfail(sys.platform == 'win32',reason = "works only in win32")
def test_str05():
    letter= "abcd"
    num = 1234
    assert letter+num == "abcd1234"


@pytest.mark.xfail
def test_str06():
    l=[1,2,3]
    m=[4,5,6]
    s=[1,2,3,4,5,6]
    assert l+m==s


