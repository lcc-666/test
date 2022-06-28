import get_grade


def get_school():
    dt = {}
    f = open("data.txt", mode="r", encoding="utf8")
    txt = f.readlines()
    for i in txt:
        item = i.strip()
        key = item.split(":")[0]
        value = item.split(":")[1]
        dt[key] = value
    return dt


if __name__ == '__main__':
    school_dt = get_school()
    print("请在data.txt查询学校代码")
    while True:
        school_id = ""
        word = input("请输入规范的学校名称或者学校代码或者q\n")
        if word is "q":
            print("感谢使用")
            exit()
        if word in school_dt.keys():
            school_id = eval(school_dt[word])
        if word in school_dt.values():
            school_id = word
        print("请选择文理")
        print({1: "理科", 2: "文科"})
        project_type = input()
        get_grade.get_num(school_id, project_type)
