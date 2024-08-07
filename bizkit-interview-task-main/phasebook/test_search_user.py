
import pytest
from .data.search_data import USERS
from .pd_search import pd_search_users,pd_sorted_search_users

@pytest.mark.parametrize("input_args, expected_result",[
   ({},USERS), # Case 1
   ({"id":"1"},[
      {"id": "1", "name": "John Doe", "age": 29, "occupation": "Developer"}
      ]), # Case 2
   ({"id":"2","name":"John"},[
  {"id": "1", "name": "John Doe", "age": 29, "occupation": "Developer"},
  {"id": "2", "name": "Jane Doe", "age": 30, "occupation": "Engineer"},
  {"id": "4", "name": "John Smith", "age": 28, "occupation": "Architect"}
]), # Case 3
({"id":"5","name":"Joe","age":30,"occupation":"Arc"},[
  {"id": "1", "name": "John Doe", "age": 29, "occupation": "Developer"},
  {"id": "2", "name": "Jane Doe", "age": 30, "occupation": "Engineer"},
  {"id": "3", "name": "Joe Doe", "age": 25, "occupation": "Designer"},
  {"id": "4", "name": "John Smith", "age": 28, "occupation": "Architect"},
  {"id": "5", "name": "Jane Smith", "age": 31, "occupation": "Manager"},
  {"id": "6", "name": "Joe Smith", "age": 24, "occupation": "Designer"}
]), # Case 4
])

def test_search_users(input_args, expected_result):
   assert pd_search_users(input_args,USERS) == expected_result

# Bonus
def test_search_users_sort():
   assert pd_sorted_search_users({"id":"5","name":"Joe","age":30,"occupation":"Arc"},USERS) ==  [
    {"id": "5", "name": "Jane Smith", "age": 31, "occupation": "Manager"},
    {"id": "3", "name": "Joe Doe", "age": 25, "occupation": "Designer"},
    {"id": "6", "name": "Joe Smith", "age": 24, "occupation": "Designer"},
    {"id": "1", "name": "John Doe", "age": 29, "occupation": "Developer"},
    {"id": "2", "name": "Jane Doe", "age": 30, "occupation": "Engineer"},
    {"id": "4", "name": "John Smith", "age": 28, "occupation": "Architect"},
  ]

