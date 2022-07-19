# We can define the fixture functions in this file to make them accessible across multiple test files.
import pytest

@pytest.fixture
def input_value():
   input = 39
   return input