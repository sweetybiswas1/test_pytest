# we can parametrized the test to run multiple arguments for a test


# Parameterizing of a test is done to run the test against multiple sets of inputs.
# We can do this by using the following marker − @pytest.mark.parametrize


import pytest

@pytest.mark.parametrize('x,y,z',[(10,20,200),(20,40,200)])
def test_method(x,y,z):
    assert x*y == z



@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output