# Student Management System

一个使用 Python 编写的简单学生成绩管理系统，用于练习 Python 模块拆分、函数设计、文件操作和 JSON 数据持久化。

## 功能

- 输入学生姓名和课程成绩
- 根据输入的课程数量收集成绩
- 检查成绩范围，处理非法输入
- 计算并显示学生平均分
- 将学生信息保存到 JSON 文件
- 程序启动时读取已有学生记录

## 项目结构

```text
Student Management System_v2/
├── data/
│   └── students.json
├── src/
│   ├── student_manager/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── student.py
│   │   ├── score.py
│   │   └── storage.py
│   └── utils/
│       ├── __init__.py
│       └── message.py
├── .gitignore
├── requirements.txt
└── README.md
```

## 运行方式

在项目根目录打开终端：

进入 `src` 目录：

```cmd
cd src
```

运行程序：

```cmd
python -m student_manager.main
```

## 数据存储

学生姓名和成绩保存在项目根目录下的 `data/students.json` 文件中。

程序会在启动时读取已有记录，并在添加学生后保存更新的数据。

## 学习目标

通过本项目练习 Python 包与模块、函数拆分、虚拟环境、文件路径、JSON 数据读写、输入校验和 Git 项目管理。
