import pickle
from helpers import Helper
from menu import Menu
from student import Student
from module import Module
import copy

class Reader:
    def save_module(module):
        data = Reader.load_data()
        data[0].append(module)
        modules = data[0]
        for x in range(0, len(modules)):
            modules[x].set_index(x)
        data[0] = modules
        with open('data.pkl', 'wb') as f:
            pickle.dump(data, f)

    def save_student(student):
        data = Reader.load_data()
        data[1].append(student)
        students = data[1]
        for x in range(0, len(students)):
            students[x].set_index(x)
        data[1] = students
        with open('data.pkl', 'wb') as f:
            pickle.dump(data, f)

    def save_students(students):
        data = Reader.load_data()
        for x in range(0, len(students)):
            students[x].set_index(x)
        data[1] = students
        with open('data.pkl', 'wb') as f:
            pickle.dump(data, f)

    def save_modules(modules):
        data = Reader.load_data()
        for x in range(0, len(modules)):
            modules[x].set_index(x)
        data[0] = modules
        with open('data.pkl', 'wb') as f:
            pickle.dump(data, f)

    def init_pickle():
        with open('data.pkl', 'wb') as f:
            pickle.dump([[], []], f)

    def load_data():
        with open('data.pkl', 'rb') as f:
            try:
                saved_data = pickle.load(f)
            except Exception as e:
                Reader.init_pickle()
                saved_data = pickle.load(f)

        return saved_data

    def get_modules():
        return Reader.load_data()[0]

    def get_students():
        return Reader.load_data()[1]

    def attach_student_to_module():
        modules = Reader.get_modules()
        selected_module = Reader.select_module(modules)

        students = Reader.get_students()
        selected_student = Reader.select_student(students)

        selected_module_assessments = selected_module.assessments
        copied_assessments = copy.deepcopy(selected_module_assessments)

        if modules[selected_module.i].has_student(selected_student.i):
            print("\nStudent already registered in that module")
            return

        for x in range(0, len(selected_module_assessments)):
            score = Reader.get_assessment_score(copied_assessments[x])
            copied_assessments[x]['score'] = score

        students[selected_student.i].set_assessments(copied_assessments)
        modules[selected_module.i].add_student(students[selected_student.i])

        Reader.save_students(students)
        Reader.save_modules(modules)

    def get_assessment_score(assessment):
        loop = True;
        while loop:
            score = input("Enter student score for " + assessment['name'] + ":")
            if not Helper.is_int(score):
                print("\nScrole should be integer")
            if score and Helper.is_int(score):
                if int(score) > 100:
                    print("\nScore can't be greater than 100")
                else:
                    loop = False
        return score

    def select_module(modules):
        selected_module = Menu.show_object(modules, ['Select Module'])
        return selected_module

    def select_student(students):
        selected_module = Menu.show_object(students, ['Select Student'])
        return selected_module

    def new_student():
        student_first_name_check = True
        student_last_name_check = True
        student_id_check = True
        while student_first_name_check or student_last_name_check or student_id_check:
            if student_first_name_check:
                student_first_name = input("First name: ")
                if student_first_name:
                    student_first_name_check = False

            if not student_first_name_check and student_last_name_check:
                student_last_name = input("Last Name: ")
                if student_last_name:
                    student_last_name_check = False
            if not student_first_name_check and not student_last_name_check and student_id_check:
                student_id = input("Student ID: ")
                if student_id:
                    student_id_check = False

        student = {'student_class': 'A', 'first_name': student_first_name, 'last_name': student_last_name, 'name': student_first_name + ' ' + student_last_name, 'student_id': student_id, 'assessments': []}
        student = Student(student)
        Reader.save_student(student)

    def new_module():
        module_name_check = True
        module_code_check = True
        should_ask_for_assessment = False
        have_valid_assessment = False
        valid_assessments_number = 0
        while module_name_check or module_code_check or should_ask_for_assessment:
            if module_name_check:
                module_name = input("Module name: ")
                if module_name:
                    module_name_check = False

            if not module_name_check and module_code_check:
                module_code = input("Module Code: ")
                if module_code:
                    module_code_check = False
                    should_ask_for_assessment = True

            if should_ask_for_assessment:
                assessments_number = input("Number of Assessments: ")
                if assessments_number:
                    valid_assessments_number = Helper.is_int(assessments_number)
                    if not valid_assessments_number:
                        print('\nInvalid, Only integer number allowed, Please enter number greater than 1')
                    else:
                        should_ask_for_assessment = False
                        have_valid_assessment = True
                        module_assessments = Reader.read_assessments(assessments_number)

        module = {'name': module_name, 'code': module_code, 'assessments': module_assessments}
        module = Module(module)
        Reader.save_module(module)

    def read_assessments(assessments_number):
        total_weight = 0
        assessments_number = int(assessments_number)
        assessments = []
        for x in range(0, assessments_number):
            print("\nData For assessment number:", x + 1)
            valid_assessment = False
            assessments_name_check = True
            assessments_weight_check = True

            while not valid_assessment:
                if assessments_name_check:
                    assessments_name = input("Assessment name: ")
                    if assessments_name:
                        assessments_name_check = False
                if not assessments_name_check and assessments_weight_check:
                    if x == (assessments_number - 1):
                        valid_int_weight = True
                        assessments_weight = 100 - total_weight
                        valid_assessment = True
                        assessments.append({'name': assessments_name, 'weight': assessments_weight})
                    else:
                        assessments_weight = input("Assessment weight: ")
                        valid_int_weight = Helper.is_int(assessments_weight)

                        if not valid_int_weight:
                            print('\nInvalid, Please enter number greated than 0 and less than 100')
                        else:
                            assessments_weight = int(assessments_weight)
                            if total_weight + assessments_weight > 100:
                                print('\nInvalid, total assessments weight can pass 100, weight available is', 100 - total_weight)
                            else:
                                assessments_weight = assessments_weight
                                total_weight += assessments_weight
                                valid_assessment = True
                                assessments.append({'name': assessments_name, 'weight': assessments_weight})

        return assessments
