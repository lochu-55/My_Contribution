from pytest_bdd import scenario,scenarios,given,when,then

import pytest
from pathlib import Path

filedir = 'myfeatures'
file = 'first101.feature'

basedir = Path(__file__).resolve().parent
featurefile = basedir.joinpath(filedir).joinpath(file)

def pytest_configure():
    pytest.AMT = 0

@scenario(featurefile,'withdrawal of money')
def test_withdrawal():
    print('end of withdrawal test')
    pass

@given('the account balance is 100')
def current_balance():
    pytest.AMT = 100

@when('the account holder withdraws 30')
def withdraw_amount():
    pytest.AMT = pytest.AMT - 30

@then('the account balance should be 70')
def final_balance():
    assert pytest.AMT == 70

@scenario(featurefile,'removal of items from set')
def test_removal():
    pass
@given('the set of 3 fruits',target_fixture="myset")
def total_fruits():
    myset = {'apple','banana','cherry'}
    return myset
@when('the remove a fruit from the set')
def remove_fruit(myset):
    myset.pop()
    print(myset)

@then('the set will have 2 fruits')
def final_set(myset):
    assert len(myset) == 2
