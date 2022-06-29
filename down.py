import pymysql


def dowb_num():
    con = pymysql.connect(host="www.chaogezuishuai.top", user="root", password="NRAHbsqt941", port=3306, db="zhang",
                          charset="utf8")
    cur = con.cursor()
    university_type = {"wen": "文科一分一段表", "li": "理科一分一段表"}
    for item in university_type.keys():
        sql = "SELECT * FROM %s" % item
        cur.execute(sql)
        result = cur.fetchall()
        f = open(file=university_type[item] + ".txt", mode="w", encoding="utf8")
        for i in result:
            num = str(i[0])
            rank = str(i[1])
            line = "分数{}，名次{}\n".format(num, rank)
            f.write(line)
        f.close()
    cur.close()
    con.close()
    print("文理科一分一段表已生成")


class two:
    def __init__(self):
        self.num = 0
        self.sign = 0


def calculation(detail: dict):
    num = detail["num"]
    hnum = detail["num"] + detail["h"]
    lnum = detail["num"] - detail["l"]
    con = pymysql.connect(host="www.chaogezuishuai.top", user="root", password="NRAHbsqt941", port=3306, db="zhang",
                          charset="utf8")
    dt = {1: "li", 2: "wen"}
    cur = con.cursor()
    ls = []
    for i in [hnum, lnum]:
        sql = "SELECT rank FROM %s where grade =%s" % (dt[detail["pro"]], i)
        cur.execute(sql)
        result = cur.fetchone()
        ls.append(result[0])

    hrank = two()
    hrank.num = ls[0]
    hrank.sign=1
    lrank = two()
    lrank.sign=1
    lrank.num = ls[1]
    rank_type = {1: "li_rank", 2: "wen_rank"}
    sql = "SELECT * FROM %s" % rank_type[detail["pro"]]
    cur.execute(sql)
    result = cur.fetchall()
    txtname=str(detail["num"])+str((hnum,lnum))+{1: "理科", 2: "文科"}[detail["pro"]]
    f=open(file=txtname,mode="w",encoding="utf8")
    f.write("2021年分数{},最低名次{}\n".format(hnum,hrank.num))
    f.write("2021年分数{},最低名次{}\n".format(lnum, lrank.num))
    for one in result:
        item=list(one)
        item.pop(0)
        while 0 in item:
            item.remove(0)
        if len(item)==1:
            if item[0]<lrank.num and item[0]>hrank.num:
                f.write(str(one)+"\n")
        if len(item) == 2:
            max_info=two()
            max_info.num=max(item)
            min_info=two()
            min_info.num=min(item)
            a=[hrank,lrank,min_info,max_info]
            a.sort(key=lambda x:x.num)
            if a[0].sign !=a[1].sign:
                f.write(str(one)+"\n")







if __name__ == '__main__':
    # dowb_num()
    num = 550
    h = 10
    l = 10
    # print({1: "理科", 2: "文科"})
    pro = 1
    info_dict = {
        "num": num,
        "h": h,
        "l": l,
        "pro": pro
    }
    calculation(info_dict)
