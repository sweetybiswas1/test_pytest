
# Whenever we need to run some code before test,we use pytest fixtures


# Fixtures are functions, which will run before each test function to which it is applied. Fixtures are used to feed some data to the tests such as database connections, URLs to test and some sort of input data. Therefore, instead of running the same code for every test, we can attach fixture function to the tests and it will run and return the data to the test before executing each test.
#
# A function is marked as a fixture by −
#
# @pytest.fixture
#
# A test function can use a fixture by mentioning the fixture name as an input parameter.


# 1.
# import pytest
#
# @pytest.fixture
# def num():
#     a=10
#     b=20
#     c=30
#     return [a,b,c]
# def test_method1(num):
#     x=15
#     assert num[0]==x
#
# def test_method2(num):
#     y=20
#     assert num[1]==y
#
# def test_method3(num):
#     z=25
#     assert num[2]==z


# 2.

import pytest

@pytest.fixture
def input_value():
   input = 39
   return input

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0



# Here, we have a fixture function named input_value, which supplies the input to the tests. To access the fixture function, the tests have to mention the fixture name as input parameter.
# Pytest while the test is getting executed, will see the fixture name as input parameter. It then executes the fixture function and the returned value is stored to the input parameter, which can be used by the test.


# However, the approach comes with its own limitation.
# A fixture function defined inside a test file has a scope within the test file only. We cannot use that fixture in another test file.
# To make a fixture available to multiple test files,
# we have to define the fixture function in a file called conftest.py. 