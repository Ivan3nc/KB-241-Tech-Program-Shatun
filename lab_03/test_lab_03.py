import pytest
from student import Student
from student_list import StudentList

def test_add_and_sort():
    sl = StudentList()
    sl.add(Student("B", "1", "1", "1"))
    sl.add(Student("A", "2", "2", "2"))
    # Має бути A, потім B
    assert sl.students[0].name == "A"
    assert sl.students[1].name == "B"

def test_delete():
    sl = StudentList()
    sl.add(Student("A", "1", "1", "1"))
    sl.delete("A")
    assert len(sl.students) == 0

def test_update():
    sl = StudentList()
    sl.add(Student("Old", "1", "1", "1"))
    sl.update("Old", Student("New", "2", "2", "2"))
    assert sl.students[0].name == "New"