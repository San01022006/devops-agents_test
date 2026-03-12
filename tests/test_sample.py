import sys
import os

# add project root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import add


def test_add():
    assert add(1, 2) == 3
