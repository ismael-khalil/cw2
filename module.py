class Module:
    def __init__(self, data):
        self.data = data
        self.name = data['name']
        self.code = data['code']
        self.assessments = data['assessments']
        self.students = []

    def avg_assessments_score(self):
        all_sum = 0
        for x in range(0, len(self.assessments)):
            try:
                all_sum += int(self.assessments[x]['score'])
            except Exception as e:
                return 0
        return all_sum

    def has_student(self, i):
        for x in range(0, len(self.students)):
            if self.students[x].i == i:
                return True
        return False


    def add_student(self, student):
        self.students.append(student)

    def get_name(self):
        return self.name

    def set_index(self, i):
        self.i = i

    def get_index(self):
        return self.i
