
from menu import Menu
from calculators import Calc
from helpers import Helper
from reader import Reader

def start():
    action_menu = [
        {"name": "Enter data", "value": "ENTER_DATA"},
        {"name": "Average score of the entire class for a specific assessment per module.", "value": "AVG_SCORE_SPECIFIC_ASSESSMENT"},
        {"name": "Average score for the module over all assessments.", "value": "AVG_SCORE_MODULE_ASSESSMENTS"},
        {"name": "Display the total score for each student per module.", "value": "TOTAL_SCORE_STUDENTS_PER_MODULE"},
        {"name": "Academic performance for each student", "value": "ACADEMIC_PERFORMANCE"},
        {"name": "Find and display the maximum/minimum score for a specific assessment/module.", "value": "MIN_MAX_ASSIGNMENT"},
        {"name": "Find and display the maximum/minimum score for the module", "value": "MIN_MAX_MODEL"},
    ]
    first_action = Menu.show(action_menu)

    if first_action['value'] == 'ENTER_DATA':
        enter_data_options = [
            {'name': 'New Module', 'value': 'NEW_MODULE'},
            {'name': 'New Student', 'value': 'NEW_STUDENT'},
            {'name': 'Attach student to module', 'value': 'ATTACH_STUDENT'},
        ]
        enter_data_option = Menu.show(enter_data_options, ['Enter Data'])
        if enter_data_option['value'] == 'NEW_MODULE':
            Reader.new_module()
        if enter_data_option['value'] == 'NEW_STUDENT':
            Reader.new_student()
        if enter_data_option['value'] == 'ATTACH_STUDENT':
            Reader.attach_student_to_module()


    if first_action['value'] == 'AVG_SCORE_SPECIFIC_ASSESSMENT':
        data = Reader.load_data()
        modules = data[0]

        choosen_module = Menu.show_object(modules)
        module_assessment = choosen_module.assessments
        selected_assessment = Menu.show(module_assessment)
        students = choosen_module.students

        result = 0
        count = 0
        for x in range(0, len(students)):
            for u in range(0, len(students[x].assessments)):
                if students[x].assessments[u]['name'] == selected_assessment['name']:
                    result += int(students[x].assessments[u]['score'])
                    count += 1
        print("Avg Result: ", (result / count))


    if first_action['value'] == 'AVG_SCORE_MODULE_ASSESSMENTS':
        data = Reader.load_data()
        modules = data[0]
        print("\n")
        for x in range(0, len(modules)):
            avg_score = modules[x].avg_assessments_score()
            print("Agv Score for module code", modules[x].code, "is:", avg_score)
        print("\n")

    if first_action['value'] == 'TOTAL_SCORE_STUDENTS_PER_MODULE':
        data = Reader.load_data()
        modules = data[0]
        choosen_module = Menu.show_object(modules)
        module_code = choosen_module.code
        students = choosen_module.students

        result = []
        for x in range(0, len(students)):
            student = students[x]
            result.append([student.first_name, student.last_name, student.assessments_score()])

        table = Helper.add_header_to_table(['First name', 'Last name', 'Total'], result)
        print('\n')
        Menu.print_student_score(table)
        print('\n')

    if first_action['value'] == 'ACADEMIC_PERFORMANCE':
        data = Reader.load_data()
        modules = data[0]
        students = data[1]

        for x in range(0, len(modules)):
            module = modules[x]
            module_students = []

            for i in range(0, len(module.students)):
                student = module.students[i]
                score = student.assessments_score()
                module_students = Helper.add_inc(module_students, student, score)


        formated_students = []

        for j in range(0, len(module_students)):
            student = module_students[j]
            percentage_score = student['score'] / len(student['student'].assessments)

            [definition, degree] = Calc.get_grade_def_degree(percentage_score)
            formated_students.append([
                student['student'].first_name,
                student['student'].last_name,
                percentage_score,
                definition,
                degree
            ])

        perf_table = Helper.add_header_to_table(['First name', 'Last name', 'Score', 'Grade Definition', 'Degree Class'], formated_students)
        print('\n')
        Menu.print_student_performance(perf_table)
        print('\n')

        ask_sort = True
        ask_sort_menu = [
            {'name': 'Sort the output alphabetically based on the first name of the students', 'value': 'SORT_FIRST'},
            {'name': 'Sort the output alphabetically based on the last name of the students', 'value': 'SORT_SECOND'},
            {'name': 'Sort the output based on the total score achieved by the student in the semester', 'value': 'SORT_SEMESTER'},
        ]
        while ask_sort:
            sort_by = Menu.show(ask_sort_menu, [], True)
            if sort_by['value'] == 'back':
                ask_sort = False
            if sort_by['value'] == 'SORT_FIRST':
                perf_table = Helper.sort_by_key(perf_table, 0)
                Menu.print_student_performance(perf_table)
            if sort_by['value'] == 'SORT_SECOND':
                perf_table = Helper.sort_by_key(perf_table, 1)
                Menu.print_student_performance(perf_table)
            if sort_by['value'] == 'SORT_SEMESTER':
                perf_table = Helper.sort_by_key(perf_table, 2)
                Menu.print_student_performance(perf_table)

    if first_action['value'] == 'MIN_MAX_ASSIGNMENT':
        modules = Reader.get_modules()
        students = Reader.get_students()
        selected_module = Menu.show_object(modules, ['Select Module'])
        selected_module_assessments = selected_module.assessments
        selected_asseessment = Menu.show(selected_module_assessments, ['Select Assessment'])
        active_students = []
        active_results = []
        for x in range(0, len(students)):
            res = students[x].assessment_score(selected_asseessment['name'])
            if res != False:
                active_students.append({'student': students[x], 'score': res})
                active_results.append(res)

        Menu.print_student_score(Helper.add_header_to_table(['Min', 'Max', ''], [[min(active_results), max(active_results), '']]))
        dshow_full = True
        action_menu_show = [
            {"name": "Show Full student data", "value": "SHOW_FULL" },
        ]
        while dshow_full:
            result = Menu.show(action_menu_show, ['Options'], True)
            if result['value'] == 'back':
                dshow_full = False
            else:
                dshow_full = False
                st = []
                for z in range(0, len(active_students)):
                    print(active_students[z])
                    st.append([
                        active_students[z]['student'].student_id,
                        active_students[z]['student'].first_name,
                        active_students[z]['student'].last_name,
                        active_students[z]['score'],
                        ''
                    ])
                Menu.print_student_performance(Helper.add_header_to_table(['ID', 'First Name', 'Last Name', 'score', ''], st))

    if first_action['value'] == 'MIN_MAX_MODEL':
        modules = Reader.get_modules()
        students = Reader.get_students()
        selected_module = Menu.show_object(modules, ['Select Module'])
        selected_module_assessments = selected_module.assessments
        # selected_asseessment = Menu.show(selected_module_assessments, ['Select Assessment'])
        active_students = []
        active_results = []
        for x in range(0, len(students)):
            res = students[x].assessments_score()
            if res != False:
                active_students.append({'student': students[x], 'score': res})
                active_results.append(res)

        Menu.print_student_score(Helper.add_header_to_table(['Min', 'Max', ''], [[min(active_results), max(active_results), '']]))
        dshow_full = True
        action_menu_show = [
            {"name": "Show Full student data", "value": "SHOW_FULL" },
        ]
        while dshow_full:
            result = Menu.show(action_menu_show, ['Options'], True)
            if result['value'] == 'back':
                dshow_full = False
            else:
                dshow_full = False
                st = []
                for z in range(0, len(active_students)):
                    print(active_students[z])
                    st.append([
                        active_students[z]['student'].student_id,
                        active_students[z]['student'].first_name,
                        active_students[z]['student'].last_name,
                        active_students[z]['score'],
                        ''
                    ])
                Menu.print_student_performance(Helper.add_header_to_table(['ID', 'First Name', 'Last Name', 'score', ''], st))


    start()

start()
