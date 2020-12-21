class Student:
    def __init__(self, data):
        self.data = data
        self.name = data['name']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.student_id = data['student_id']
        self.student_class = data['student_class']
        self.assessments = data['assessments']

    def set_assessments(self, assessments):
        self.assessments = assessments

    def add_assessment(self, assessment):
        self.assessments.append(assessment)

    def assessments_score(self):
        total = 0
        for x in range(0, len(self.assessments)):
            total += int(self.assessments[x]['score'])
        return total

    def assessment_score(self, assessment_name):
        for x in range(0, len(self.assessments)):
            if self.assessments[x]['name'] == assessment_name:
                return self.assessments[x]['score']

        return False


    def get_name(self):
        return self.name

    def set_index(self, i):
        self.i = i

    def get_index(self):
        return self.i
