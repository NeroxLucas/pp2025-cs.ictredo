def option(answer, st, course):
    if answer == 1:  
        st_name = input("Student Name: ")
        st_id = input("Student ID: ")
        st[st_id] = st_name
    elif answer == 2:  
        course_name = input("Course Name: ")
        course_id = input("Course ID: ")
        course[course_id] = {"name": course_name, "students": {}}
    elif answer == 3:  
        c_id = input("Course ID: ")
        s_id = input("Student ID: ")
        mark = input("Mark: ")
        if c_id in course and s_id in st:
            course[c_id]["students"][s_id] = mark
            print(f"Mark {mark} assigned to student {s_id} in course {c_id}")
        else:
            print("Invalid course or student ID.")
    else:
        print("Invalid option")


def print_func(st, course):
    print("\nStudent Info:")
    for st_id, st_name in st.items():
        print(f"Student: {st_name}, ID: {st_id}")

    print("\nCourse Info:")
    for course_id, details in course.items():
        print(f"Course: {details['name']}, ID: {course_id}")
        if details["students"]:
            print("Marks:")
            for student_id, mark in details["students"].items():
                print(f"  Student ID: {student_id}, Name: {st[student_id]}, Mark: {mark}")
        else:
            print("  No students enrolled in this course.")


if __name__ == "__main__":
    st = {}  
    course = {}  
    
    while True:
        answer = int(input(
            "\nChoose option:\n"
            "1: Input student info\n"
            "2: Input course info\n"
            "3: Input mark info\n"
            "4: Print info\n"
            "5: Exit\nYour option: "
        ))
        if answer == 5:
            print("Goodbye!")
            break
        elif answer == 4:
            print_func(st, course)
        elif answer in (1, 2, 3):
            option(answer, st, course)
        else:
            print("Invalid option. Please choose between 1 and 5.")
