all_courses = ['Python', 'Java', 'Machine Learning', 'Big data', 'C programming', 'Oracle SQL', 'Power Bi', 'Go lang',
               'C++ Graphics', 'React JS', 'Ruby Rails', 'Flask', 'HTML & CSS', 'Salesforce', 'Javascript', 'Django']

name = input("Enter the name : ")
email = input("Enter the mail_id : ")
courses = []


def user_info():
    user = {
        "Name": name,
        "Email": email,
        "My_courses": courses
    }
    return user


def menu_prompt():
    menu = int(input('''
1. All courses
2. My courses
3. Show profile
4. remove course from my courses
0. Exit '''))
    return menu


def select_courses():
    print(all_courses)
    selected_course = input("select the course from the above list split by ',' : ").strip().lower().split(",")
    for data in selected_course:
        value = erase_courses(data)
        if value != 0:
            courses.extend(selected_course)


def erase_courses(del_course):
    for index, course in enumerate(all_courses):
        if del_course == course.lower():
            del all_courses[index]
            break
    else:
        print(f"{del_course} is not found in the list Please select the courses from available set of courses")
        return 0


def add_courses(add_course):
    all_courses.append(add_course)


def remove_course():
    print("select the course from the below displayed list")
    display_mycourses()
    del_course = input("enter the course to remove from user course ").lower()
    add_courses(del_course)
    for index, course in enumerate(courses):
        if del_course == course.lower():
            del courses[index]


def display_profile():
    userdata = user_info()
    for key, value in userdata.items():
        if key == "My_courses":
            value = list(value)
            value = ",".join(value)
            print(key, "=", value)
        else:
            print(key, "=", value)


def user_courses():
    display_mycourses()
    removecourse = input("do you want to erse any course press any button else press enter : ")
    if len(removecourse) != 0:
        remove_course()


def display_mycourses():
    userdata = user_info()
    for key, value in userdata.items():
        if key == "My_courses":
            values = list(value)
            print(f"Enrolled courses are : ")
            for index, data in enumerate(values):
                print(f"{index + 1}. {data}")


while True:
    user_input = menu_prompt()
    if user_input == 0:
        break
    elif user_input == 1:
        select_courses()
    elif user_input == 2:
        user_courses()
    elif user_input == 3:
        display_profile()
    elif user_input == 4:
        remove_course()
    else:
        print("please enter the valid option")
