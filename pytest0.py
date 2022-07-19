import math
import pytest

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def testsquare():
   num = 7
   assert 7*7 == 40

def tesequality():
   assert 10 == 11



# See the first line of the result. It displays the file name and the results. F represents a test failure and dot(.) represents a test success.
# Below that, we can see the details of the failed tests. It will show at which statement the test has failed. In our example, 7*7 is compared for equality against 40, which is wrong. In the end, we can see test execution summary, 1 failed and 1 passed.
# The function tesequality is not executed because pytest will not consider it as a test since its name is not of the format test*

# pytest = run tests from all the files

# pytest -v
# -v increases the verbosity.

# Note − pytest command will execute all the files of format test_* or *_test in the current directory and subdirectories.

# To execute the tests from a specific file, use the following syntax −pytest <filename> -v

