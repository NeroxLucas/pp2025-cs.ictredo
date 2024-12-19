def get_student_info(stdscr):
    stdscr.addstr("Enter student name: ")
    stdscr.refresh()
    name = stdscr.getstr().decode("utf-8").strip()

    stdscr.addstr("Enter student ID: ")
    stdscr.refresh()
    student_id = stdscr.getstr().decode("utf-8").strip()

    return name, student_id


def get_course_info(stdscr):
    stdscr.addste("Enter course name: ")
    stdscr.refresh()
    name = stdscr.getstr().decode("utf-8").strip()

    stdscr.addste("Enter course ID: ")
    stdscr.refresh()
    course_id = stdscr.getstr().decode("utf-8").strip()
    return name, course_id

def get_mark_info(stdscr):
    stdscr.addste("Enter student ID: ")
    stdscr.refresh()
    student_id = stdscr.getstr().decode("utf-8").strip()

    stdscr.addste("Enter course ID: ")
    stdscr.refresh()
    course_id = stdscr.getstr().decode("utf-8").strip()

    stdscr.addste("Enter mark: ")
    stdscr.refresh()
    mark = stdscr.getstr().decode("utf-8").strip()
    return student_id, course_id, round(mark, 1)
