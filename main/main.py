import sqlite3

db = sqlite3.connect('university.db')

db.execute('''CREATE TABLE IF NOT EXISTS students (
           student_id INTEGER PRIMARY KEY AUTOINCREMENT,
           name VARCHAR(50),
           age INTEGER,
           major VARCHAR(50));
''')

db.execute('''CREATE TABLE IF NOT EXISTS courses (
           course_id INTEGER PRIMARY KEY AUTOINCREMENT,
           course_name VARCHAR(50),
           instructor VARCHAR(50));
''')

db.execute('''
        CREATE TABLE IF NOT EXISTS student_courses (
        student_id INTEGER,
        course_id INTEGER,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES students (student_id) ON DELETE CASCADE,
        FOREIGN KEY (course_id) REFERENCES courses (course_id) ON DELETE CASCADE);
''')


def add_user(db, name, age, major):
    db.execute(f'''INSERT INTO students(name, age, major)
               VALUES (?, ?, ?)''', (name, age, major))
    db.commit()

def add_course(db, course_name, instructor):
    db.execute(f'''INSERT INTO courses(course_name, instructor)
               VALUES (?, ?)''', (course_name, instructor))
    db.commit()

def add_student_to_course(db, student_id, course_id):
    db.execute('''INSERT INTO student_courses(student_id, course_id)
                VALUES (?, ?)''', (student_id, course_id))
    db.commit()

def get_student_courses(db, course_id):
    return db.execute('''
        SELECT students.name
        FROM students
        JOIN student_courses ON students.student_id = student_courses.student_id
        WHERE student_courses.course_id = ?
    ''', (course_id,)).fetchall()


while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7): ")

    match choice:
        case "1":
            add_user(db, input("Введіть ім'я студента: "), input("Введіть вік студента: "), input("Введіть факультет: "))
            print(f"Студента додано успішно.")

        case "2":
            add_course(db, input("Введіть назву курсу: "), input("Введіть викладача курсу: "))
            print(f"Курс додано успішно.")

        case "3":
            print("Список студентів: ", db.execute('''SELECT * FROM students''').fetchall())

        case "4":
            print("Список курсів: ", db.execute('''SELECT * FROM courses''').fetchall())

        case "5":
            try:
                add_student_to_course(db, input("Введіть id студента: "), input("Введіть id курсу: "))
                print(f"Студента до курсу додано успішно.")
            except sqlite3.IntegrityError:
                print("Студент вже записаний на цей курс.")
        
        case "6":
            course_id = int(input("Введіть id курсу: "))
            print("Студенти на курсі: ", get_student_courses(db, course_id))
            

        case "7":
            break

        case _:
            print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")
