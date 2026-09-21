from student_manager.score import average,get_scores,get_course_number
from utils.message import hello

def main():
    name = input("请输入姓名：")
    hello(name)

    course_num = get_course_number()

    print(f"请分别输入{course_num}门课程的成绩".center(40, "-"))
    scores = get_scores(course_num)

    result = average(scores)
    print(f"平均分为：{result}")

if __name__ == "__main__":
    main()
