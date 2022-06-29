import get_grade
import down

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


def get_school_grade():
    school_dt = get_school()
    print("请在data.txt查询学校代码")
    while True:
        school_id = ""
        word = input("请输入规范的学校名称或者学校代码或者q\n")
        if word is "q":
            print("退出查询学校历年分数")
            return
        if word in school_dt.keys():
            school_id = eval(school_dt[word])
        elif word in school_dt.values():
            school_id = word
        else:
            print("输入格式错误请重新输入")
            continue
        print("请选择文理")
        print({1: "理科", 2: "文科"})
        project_type = input()
        get_grade.get_num(school_id, project_type)

def get_down():
    down.dowb_num()
    num = input("请输入你的分数\n")
    h = input("输入增加的上限\n")
    l = input("输入减少的下限\n")
    print({1: "理科", 2: "文科"})
    pro = input("请选择文理\n")
    info_dict = {
        "num": int(num),
        "h": int(h),
        "l": int(l),
        "pro": int(pro)
    }
    down.calculation(info_dict)
    print("分析完成,请查看结果\n")

if __name__ == '__main__':
    while True:
        print("1.查询学校历年分数\n2.查询可报考学校\nq.退出程序")
        word=input("请选择查询模式\n")
        if word =="1":
            get_school_grade()
        elif word =="2":
            get_down()
        elif word is "q":
            print("感谢使用")
            break
        else:
            print("输入错误请重新输入")
            continue



