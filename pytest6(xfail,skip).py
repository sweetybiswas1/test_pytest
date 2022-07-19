# Now, consider the below situations −
#
#     A test is not relevant for some time due to some reasons.
#     A new feature is being implemented and we already added a test for that feature.
#
# In these situations, we have the option to xfail the test or skip the tests.
#
# Pytest will execute the xfailed test, but it will not be considered as part failed or passed tests. Details of these tests will not be printed even if the test fails (remember pytest usually prints the failed test details). We can xfail tests using the following marker −
#
# @pytest.mark.xfail
#
# Skipping a test means that the test will not be executed. We can skip tests using the following marker −
#
# @pytest.mark.skip
#
# Later, when the test becomes relevant we can remove the markers.

import pytest

@pytest.fixture
def num():
    a=10
    b=20
    c=30
    return [a,b,c]

@pytest.mark.xfail
def test_method1(num):
    x=15
    assert num[0]==x

@pytest.mark.skip
def test_method2(num):
    y=20
    assert num[1]==y

def test_method3(num):
    z=30
    assert num[2]==z


@pytest.mark.xfail
@pytest.mark.great
def test_greater():
   num = 100
   assert num > 100

@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100

@pytest.mark.skip
@pytest.mark.others
def test_less():
   num = 100
   assert num < 200