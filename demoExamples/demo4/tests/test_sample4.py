
import pytest
import sys

@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires python3.7 or higher")
def test_example():
    assert 1 == 1
