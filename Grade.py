from audioop import avg


class Grade:
    grade_current_index = 0
    sum_grades = 0
    list_of_topics = ['math', 'python', 'english']

    def __init__(self, student_name, grade, topic):
        self.__topic = None
        self.__grade = 0
        self.__student_name = student_name
        self.set_topic(topic)
        self.set_grade(grade)
        Grade.grade_current_index += 1
        self.__grade_index = Grade.grade_current_index
        Grade.sum_grades = Grade.sum_grades + self.__grade

    @staticmethod
    def get_average():
        avg = Grade.sum_grades / Grade.grade_current_index
        return avg

    @staticmethod
    def get_grade_current_index():
        return Grade.grade_current_index

    def is_grade_higher_than_avg(self):
        if self.__grade > Grade.get_average():
            print('Your grade is higher than the average!!!')
            return True
        else:
            return False

    def get_grade(self):
        return self.__grade

    def set_grade(self, new_grade):
        if 0 > new_grade > 100:
            print('Grade is invalid, not changing.')
        else:
            self.__grade = new_grade

    def get_student_name(self):
        return self.__student_name

    def get_grade_index(self):
        return self.__grade_index

    def set_topic(self, new_topic):
        if new_topic not in Grade.list_of_topics:
            print(f'Invalid topic [{new_topic}], please choose another')
        else:
            self.__topic = new_topic

    def get_topic(self):
        return self.__topic

    def __str__(self):
        return f'Student name: {self.get_student_name()} Topic: {self.get_topic()} Grade: {self.get_grade()}' \
               f' Grade index: {self.get_grade_index()} Is higher than average: {self.is_grade_higher_than_avg()} '\
               f' Sum of all grades: {Grade.sum_grades} Grades current index: {Grade.get_grade_current_index()}'\
               f' Current average is: {Grade.get_average()}'

    def __repr__(self):
        return str(self.__dict__)
