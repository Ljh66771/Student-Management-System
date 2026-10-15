from student_manager.score import average

def create_student(name,scores):
    student = {}
    student['name'] = name
    student['scores'] = scores
    return student

def get_student_average(student):
    scores = student['scores']
    return average(scores)
