import ast
import inspect
import unittest

from do_not_modify.data_zad2 import students
from zad2 import *


def is_for_in_method_body(func):
    source = inspect.getsource(func)
    module = ast.parse(source)
    for node in module.body:
        if isinstance(node, ast.FunctionDef) and node.name == func.__name__:
            for sub_node in ast.walk(node):
                if isinstance(sub_node, ast.For):
                    return True
    return False


class TestZad1(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_total_grades(students), 160)
        self.assertFalse(is_for_in_method_body(get_total_grades))

    def test_2(self):
        self.assertEqual(get_total_age_of_science_students(students), 63)
        self.assertFalse(is_for_in_method_body(get_total_age_of_science_students))

    def test_3(self):
        excellent_students = get_students_with_excellent_grades(students)
        for student in excellent_students:
            self.assertTrue(student.grades.count(5) > 2)
        self.assertFalse(is_for_in_method_body(get_students_with_excellent_grades, ))

    def test_4(self):
        sorted_students = get_students_sorted_by_grades(students)
        for i in range(len(sorted_students) - 1):
            self.assertTrue(mean(sorted_students[i].grades) >= mean(sorted_students[i + 1].grades))
        self.assertFalse(is_for_in_method_body(get_students_sorted_by_grades))

    def test_5(self):
        better_students = get_better_grades(students)
        for student in better_students:
            for grade in student.grades:
                self.assertTrue(grade > 1 and grade <= 5)
        self.assertFalse(is_for_in_method_body(get_better_grades))


if __name__ == '__main__':
    unittest.main()
