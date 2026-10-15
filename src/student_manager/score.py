def average(scores):    #计算平均成绩
    return sum(scores) / len(scores)

def check_score(number):   #检查成绩合法性
    return 0 <= number <= 100

def check_course_number(number):    #检查课程数量合法性
    return number > 0

def get_course_number():    #获取课程数并判断输入合法性
    while True:
        try:
            num = int(input("请输入课程数量："))
        except ValueError:
            print("请输入数字！")
            continue
        if check_course_number(num):
            return num
        print("课程数量必须大于0")

def get_valid_score():  #获取成绩并判断输入合法性
    while True:
        try:
            score = int(input("请输入成绩："))
        except ValueError:
            print("请输入数字！")
            continue
        if check_score(score):
            return score
        print("成绩必须在 0~100")


def get_scores(count):  #获取成绩列表
    scores = []

    for i in range(count):
        scores.append(get_valid_score())
    return scores