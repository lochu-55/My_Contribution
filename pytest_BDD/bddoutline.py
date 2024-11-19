from pytest_bdd import parsers,scenario,scenarios,given,when,then

import pytest
from pathlib import Path

filedir = 'myfeatures'
file = 'ScenarioOutline.feature'

basedir = Path(__file__).resolve().parent
featurefile = basedir.joinpath(filedir).joinpath(file)

@scenario(featurefile,'scene outline test')
def test_outline():
    pass

@given(parsers.parse("there are {start:d} cucumbers"),target_fixture="cucumbers")
def existing_cucumbers(start):
    return dict(start=start)

@when(parsers.parse('I deposit {deposit:d} cucumbers'))
def deposit_cucumbers(cucumbers,deposit):
    cucumbers['deposit'] = deposit

@when(parsers.parse('I withdraw {withdraw:d} cucumbers'))
def deposit_cucumbers(cucumbers,withdraw):
    cucumbers['withdraw'] = withdraw
    print(cucumbers)

@then(parsers.parse('I should have {final:d} cucumbers'))
def final_cucumbers(cucumbers,final):
    assert cucumbers['start']  + cucumbers['deposit'] - cucumbers['withdraw'] == final

