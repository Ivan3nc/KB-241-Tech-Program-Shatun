import pytest
from Student import Student
from StudentList import StudentList

def test_add_student_sorted():
    sl = StudentList()

    s1 = Student("Borys", "1", "1", "1")
    s2 = Student("Andrii", "2", "2", "2")
    s3 = Student("Clara", "3", "3", "3")
    
    sl.add(s1)
    sl.add(s2)
    sl.add(s3)
    
    all_students = sl.get_all()
    
    assert all_students[0].name == "Andrii"
    assert all_students[1].name == "Borys"
    assert all_students[2].name == "Clara"

def test_delete_student():
    sl = StudentList()
    sl.add(Student("Andrii", "1", "1", "1"))
    sl.add(Student("Borys", "2", "2", "2"))
    
    sl.delete("Andrii")
    
    all_students = sl.get_all()
    assert len(all_students) == 1
    assert all_students[0].name == "Borys"