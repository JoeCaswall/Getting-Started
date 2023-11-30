from employee import Employee
import pytest

@pytest.fixture
def tester_employee():
    emma = Employee("Emma", "Robinson", 80_000)
    return emma

def test_give_default_raise(tester_employee):
    tester_employee.give_raise()
    assert tester_employee.salary == 85_000

def test_give_custom_raise(tester_employee):
    tester_employee.give_raise(10_000)
    assert tester_employee.salary == 90_000

