class Student:
    def __init__(self, name, age, grades, school, major, email):
        self.name = name
        self.age = age
        self.grades = grades  # Lista ocen
        self.school = school  # Szkoła
        self.major = major  # Kierunek studiów
        self.email = email  # Email

students = [
    Student("John", 15, [5, 5, 4, 4], "Military University of Technology", "Science", "john@example.com"),
    Student("Sarah", 16, [4, 4, 3, 3], "Military University of Technology", "Arts", "sarah@example.com"),
    Student("Tom", 15, [5, 5, 5, 5], "Military University of Technology", "Mathematics", "tom@example.com"),
    Student("Alice", 16, [3, 3, 3, 3], "Military University of Technology", "Science", "alice@example.com"),
    Student("Mark", 17, [4, 4, 4, 4], "Warsaw University of Technology", "Mathematics", "mark@example.com"),
    Student("Emma", 16, [5, 5, 5, 5], "Warsaw University of Technology", "Science", "emma@example.com"),
    Student("Oliver", 15, [3, 3, 3, 3], "Warsaw University of Technology", "Arts", "oliver@example.com"),
    Student("Sophia", 16, [4, 4, 4, 4], "Warsaw University of Technology", "Science", "sophia@example.com"),
    Student("Lucas", 17, [5, 5, 5, 5], "Warsaw University of Technology", "Mathematics", "lucas@example.com"),
    Student("Ava", 16, [1, 3, 3, 3], "Warsaw University of Technology", "Arts", "ava@example.com"),
]
