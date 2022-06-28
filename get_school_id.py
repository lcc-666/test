import pymysql
import requests
import time
import main
import tqdm
"""
https://api.eol.cn/web/api/&page=2&request_type=1&size=20&uri=apidata/api/gk/school/lists
https://api.eol.cn/web/api/?page=3&request_type=1&size=20&uri=apidata/api/gk/school/lists
"""


# header = {
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 "
#                   "Safari/537.36 Edg/101.0.1210.39 "
# }
#
# for i in range(1,143):
#     url="https://api.eol.cn/web/api/?page=%d&request_type=1&size=20&uri=apidata/api/gk/school/lists"%i
#     txt = requests.get(url=url, headers=header, ).json()
#     item=txt["data"]["item"]
#
#     f=open(file="./data.txt",mode="a")
#     for one in item:
#         f.write(one["name"]+":"+str(one["school_id"])+"\n")
#     time.sleep(1)
#     print(i)

def get_xian():
    a = []
    f = open(file="item.txt", mode="r")
    nei = f.readlines()
    while nei:
        a.append(nei[0].strip())
        nei.pop(0)
        nei.pop(0)
        a.append(nei[0].strip())
        nei.pop(0)

    f = open("result.txt", mode="a")
    for i in range(len(a)):
        if i % 2 != 0:
            f.write(a[i])
            f.write("\n")
        else:
            f.write(a[i] + " ")


def sql():
    f = open(file="result.txt", mode="r")
    a = f.readlines()
    con = pymysql.connect(host="www.chaogezuishuai.top", user="root", password="NRAHbsqt941", port=3306, db="zhang",
                          charset="utf8")
    cur = con.cursor()
    sql = "INSERT INTO wen VALUES (%s,%s)"
    for item in a:
        grade=item.split()[0]
        rank=item.split()[1]
        args=(grade,rank)
        cur.execute(sql,args)
        con.commit()
    cur.close()
    con.close()


def get_num(i:tuple, j):
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 "
                      "Safari/537.36 Edg/101.0.1210.39 "
    }
    dt = {1: "理科", 2: "文科"}
    try:
        url = "https://static-data.gaokao.cn/www/2.0/schoolprovinceindex/2021/{}/14/{}/1.json".format(i[1], j)
        txt = requests.get(url=url, headers=header, ).json()
        item = txt['data']["item"]
    except TypeError:
        s=open(file="error.txt",mode="a",encoding="utf8")
        s.write(str(i)+"\n")
        return


    item_dict = {
        "本科一批A段": 0,
        "本科一批B段": 0,
        "本科二批A段": 0,
        "本科二批B段": 0,
    }
    for one in item:
        item_dict[one["local_batch_name"]] = int(one["min_section"])

    f = open(file="result.txt", mode="a",encoding="utf8")
    f.write(i[0]+" "+str(item_dict)+"\n")


def sql_info():
    f=open(file="result.txt",mode="r",encoding="utf8")
    info=f.readlines()
    a12=[]
    for item in info:
        item=item.strip()
        ls=item.split(maxsplit=1)
        school_name=ls[0]
        dt=eval(ls[1])
        if sum(dt.values())==0:
            continue
        vlaues=list(dt.values())
        while len(vlaues)>4:
            vlaues.pop()
        tu=tuple([school_name]+vlaues)
        a12.append(tu)


    con = pymysql.connect(host="www.chaogezuishuai.top", user="root", password="NRAHbsqt941", port=3306, db="zhang",
                          charset="utf8")
    cur = con.cursor()
    sql = "INSERT INTO li_rank VALUES (%s,%s,%s,%s,%s)"
    for i in tqdm.tqdm(a12):
        cur.execute(sql,i)
        con.commit()
    cur.close()
    con.close()



if __name__ == '__main__':
    sql_info()
