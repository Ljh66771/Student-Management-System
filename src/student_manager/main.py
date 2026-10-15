from student_manager.score import average,get_scores,get_course_number
from utils.message import hello
from student_manager.student import create_student,get_student_average
from student_manager.storage import save_students,load_students

def main():
    students = load_students()  #读取学生列表数据
    print(f"当前有{len(students)}名学生")     #输出当前学生信息
    for student in students:
        print(f"姓名：{student["name"]}"
              f"成绩：{student['scores']}"
              f"平均分：{get_student_average(student)}")

    name = input("请输入姓名：")  #输入姓名
    hello(name)

    course_num = get_course_number()    #获取课程数量

    print(f"请分别输入{course_num}门课程的成绩".center(40, "-"))
    scores = get_scores(course_num)     #获取各个课程成绩

    result = average(scores)    #计算平均分
    print(f"平均分为：{result}")

    student = create_student(name, scores)  #创建学生信息
    students.append(student)
    save_students(students)     #保存学生信息
    print("保存成功")

if __name__ == "__main__":
    main()
