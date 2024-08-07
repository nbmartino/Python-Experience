
import pytest
from .data.match_data import MATCHES
from .match import is_match

@pytest.mark.parametrize("match_id, expected_result",[
   (0, True), # Case 1
   (1, False), # Case 2
   (2, True), # Case 3
   (3, False), # Case 4
])

def test_match(match_id, expected_result):
   assert is_match(*MATCHES[match_id]) == expected_result


