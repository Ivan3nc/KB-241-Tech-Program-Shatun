import pytest
from lab_02 import find_insert_position, student_list

def setup_module(module):
    student_list.clear()
    student_list.extend([
        {"name": "Andrii", "phone": "...", "group": "...", "email": "..."},
        {"name": "Dmytro", "phone": "...", "group": "...", "email": "..."},
        {"name": "Oksana", "phone": "...", "group": "...", "email": "..."}
    ])

def test_insert_start():
    assert find_insert_position("Alex") == 0

def test_insert_middle():
    assert find_insert_position("Borys") == 1

def test_insert_end():
    assert find_insert_position("Yulia") == 3