class Calc:
    def avg_score_assessment(data):
        all_sum = 0
        for x in range(0, len(data)):
            print(data)
            try:
                all_sum += data[x]['score']
            except Exception as e:
                return 0


        return all_sum / len(data)

    def total_score_assessment(data):
        all_sum = 0
        for x in range(0, len(data)):
            all_sum += data[x]['score']

        return all_sum

    def get_grade_def_degree(score):
        if score >= 70:
            return ['Excellent to Outstanding', 'First']
        if score >= 60 and score <= 69:
            return ['Good to Very Good', 'Upper Second 2:1']
        if score >= 50 and score <= 59:
            return ['Satisfying', 'Lower Second 2:2']
        if score >= 40 and score <= 49:
            return ['Sufficient', 'Third 3']

        return ['Unsatisfactory', 'Fail']
