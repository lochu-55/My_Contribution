from pytest_bdd import scenario,scenarios,given,when,then
from pathlib import Path
import pytest

filedir = 'myfeatures'
file = 'fixtures.feature'

basedir = Path(__file__).resolve().parent
featurefile = basedir.joinpath(filedir).joinpath(file)

scenarios(featurefile)

@pytest.fixture()
def setup_set():
    print("\nthe fixture...setup() function..\n")
    countries = {'poland','america','india','canada','germany'}
    return countries

@given('A datatype set')
def check_set_type(setup_set):
    print("in background")
    if not isinstance(setup_set,set):
        pytest.xfail("the type is not a set type")

@given('the set is not empty')
def check_set_notempty(setup_set):
    print('in background checking non empty set')
    if len(setup_set) == 0:
        pytest.xfail("the set of elements is empty")


@given('A set with 3 elements',target_fixture='setup_set1')
def set_of_ele(setup_set):
    if len(setup_set) == 0:
        pytest.xfail("the set of elements is empty")
    elif len(setup_set) > 3:
        while len(setup_set) > 3:
            setup_set.pop()
    return setup_set


@when('add 2 elements to the set')
def add_element(setup_set1):
    setup_set1.add('nepal')
    setup_set1.add('UK')

@then('the set should have 5 elements')
def final_set_elements(setup_set1):
    print(setup_set1)
    assert len(setup_set1) == 5