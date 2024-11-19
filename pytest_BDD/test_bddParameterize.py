from pytest_bdd import scenario,scenarios,given,when,then,parsers
from pathlib import Path
import pytest

filedir = 'myfeatures'
file = 'parameterize.feature'

basedir = Path(__file__).resolve().parent
featurefile = basedir.joinpath(filedir).joinpath(file)

scenarios(featurefile)

@given('there are 3 varieties of fruits',target_fixture='fruits')
def existing_fruit():
    fruits = {'apple','banana','orange'}
    return fruits
@when('we add a same variety of fruit')
def add_fruit(fruits):
    fruits.add('apple')

@then('there is same count of varieties')
def same_count(fruits):
    assert len(fruits) == 3

@then('if we add a different variety of fruit')
def add_diff_variety(fruits):
    fruits.add('cherry')

@then(parsers.parse('the count of varieties increases of {count:d}') )
def count_increases(fruits,count):
    print(fruits)
    assert len(fruits) == count


#####################   end of first test   ####################
pytest.total_fruits = 0;

@given(parsers.parse('given there are {count:d} fruits'),target_fixture='start_fruits')
def existing_fruits(count):
    pytest.total_fruits = count
    return dict(start=count,eat=0)

@when(parsers.parse('I eat {eat:d} fruits'))
def eat_fruits(start_fruits,eat):
    start_fruits['eat'] += eat
    print(start_fruits)

@then(parsers.parse('I should have {left:d} fruits'))
def left_fruits(start_fruits,left):
    assert start_fruits['start'] == pytest.total_fruits
    assert start_fruits['start'] - start_fruits['eat'] == left