"""This is a program Docstring"""
def main():
    """This is a function Docstring"""
    student_id = input()
    if len(student_id) == 8:
        if student_id[2] == '1' and student_id[3] == '6':
            print("yes")
        else:
            print("no")
    else:
        print("no")
main()
