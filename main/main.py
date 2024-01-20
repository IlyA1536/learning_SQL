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

db.execute('''
        INSERT INTO students(name, age, major)
        VALUES
        ('John2', 13, 'Major2');
''')

db.execute('''
        INSERT INTO courses(course_name, instructor)
        VALUES
        ('Math', 'Bob');
''')

db.commit()

while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7): ")

    if choice == "1":
        pass

    elif choice == "2":
        pass

    elif choice == "3":
        pass
     
    elif choice == "4":
        pass

    elif choice == "5":
        pass

    elif choice == "6":
        pass
       
    elif choice == "7":
        break

    else:
        print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")