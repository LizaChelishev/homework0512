class Grade:
    sum_grades = 0
    grade_index = 1
    list_of_topics = ['math', 'pyhton', 'english']

    def __init__(self, student_name, topic, garde):
        self.grade_index = Grade.grade_index
        Grade.grade_index += 1
        self.__student_name = student_name
        self.__topic = topic
        self.__grade = garde
        Grade.sum_grades = Grade.sum_grades + self.__grade

    @staticmethod
    def get_average():
        avg = Grade.sum_grades / Grade.grade_index
        return avg

    @staticmethod
    def get_current_index(grade_index):
        return grade_index

    def is_grade_higher_than_avg(self, avg, __grade):
        if avg > self.__grade:
            print('Your grade is higher than the average!!!')

    def get_grade(self):
        return self.__grade

    def set_grade(self, new_grade):
        if 0 > new_grade > 100:
            print('Grade is invalid, not changing.')
        self.__grade = new_grade

    def get_student_name(self):
        return self.__student_name

    def get_grade_index(self):
        return Grade.grade_index

    def set_topic(self, list_of_topics, new_topic):
        if self.__topic not in list_of_topics:
            print('Invalid topic, please choose another')
        self.__topic = new_topic

    def get_topic(self):
        return self.__topic

    def __str__(self):
        return f'Student name:{self.__student_name} topic:{self.__topic}  grade:{self.__grade}' \
        f'   Grade index: {Grade.grade_index} Sum of all grades:{Grade.sum_grades}'

    def __repr__(self):
        return str(self.__dict__)