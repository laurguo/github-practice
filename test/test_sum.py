import pytest 
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from sum import sum

def test_sum():
    assert sum(6, 7) == 13
    assert sum(14, -3) == 11