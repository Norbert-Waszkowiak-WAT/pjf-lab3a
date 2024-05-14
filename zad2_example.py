# Napisz funkcję get_older_students(students), która zwraca listę studentów, których wiek został zwiększony o 1 rok.
# Używamy map z wyrażeniem lambda do zwiększenia wieku każdego studenta o 1 rok
from statistics import mean

from do_not_modify.data_zad2 import Student

def get_older_students(students):
    return list(map(lambda student: Student(student.name, student.age + 1, student.grades), students))


# Napisz funkcję get_students_with_good_grades(students), która zwraca listę studentów, którzy mają średnią ocen wyższą niż 4.
# Używamy filter z wyrażeniem lambda do znalezienia wszystkich studentów, którzy mają średnią ocen wyższą niż 4
def get_students_with_good_grades(students):
    return list(filter(lambda student: mean(student.grades) > 4, students))

# Napisz funkcję get_students_sorted_by_name(students), która zwraca listę studentów posortowaną według ich imienia, od A do Z.
# Używamy sorted z wyrażeniem lambda do posortowania studentów według ich imienia, od A do Z
def get_students_sorted_by_name(students):
    return sorted(students, key=lambda student: student.name)