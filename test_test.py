import pytest
import allure

@pytest.allure.step
def make_test_data_foo():
    pass

def test_foo():
    assert make_some_data_foo() is not None

@pytest.allure.step('make_some_data_foo')
def make_some_data_bar():
    pass

def test_bar():
    assert make_some_data_bar() is not None
