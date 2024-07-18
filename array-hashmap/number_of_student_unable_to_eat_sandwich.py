def countStudents(students, sandwiches):
    n = len(students)
    m = len(sandwiches)
    while sandwiches:
        if students[0] != sandwiches[0]:
            if students == students[1:] + [students[0]]:
                break
            students.append(students[0])
            students.pop(0)
        else:
            students.pop(0)
            sandwiches.pop(0)
    return len(sandwiches)