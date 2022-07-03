"""
理科1a
https://static-data.gaokao.cn/www/2.0/schoolplanindex/2022/269/14/1/51/1.json
https://static-data.gaokao.cn/www/2.0/schoolplanindex/2022/269/14/2/51/1.json
理科1b
https://static-data.gaokao.cn/www/2.0/schoolplanindex/2022/269/14/1/52/1.json
理科2a
https://static-data.gaokao.cn/www/2.0/schoolplanindex/2022/269/14/1/44/1.json
理科2b
https://static-data.gaokao.cn/www/2.0/schoolplanindex/2022/269/14/1/45/1.json
"""
import time
import requests

def get_school():
    dt = {}
    f = open("data.txt", mode="r", encoding="utf8")
    txt = f.readlines()
    for i in txt:
        item = i.strip()
        key = item.split(":")[1]
        value = item.split(":")[0]
        dt[key] = value
    return dt




def get_new_major(schiil_id, j):
    type_dt = {"1": "理科", "2": "文科"}
    dt = {
        "51": "1A",
        "52": "1B",
        "44": "2A",
        "45": "2B"
    }
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 "
                      "Safari/537.36 Edg/101.0.1210.39 "
    }

    school_dt=get_school()
    f = open(file=(school_dt[str(schiil_id)])+" " + type_dt[j] + ".txt", mode="a", encoding="utf8")
    f.write("\n\n")
    f.write("2022山西计划招生\n")
    for i in dt.keys():
        f.write(dt[i] + "\n")
        x = 0
        while x < 10:
            x += 1
            url = "https://static-data.gaokao.cn/www/2.0/schoolplanindex/2022/{}/14/{}/{}/{}.json".format(schiil_id,
                                                                                                             j, i, x)
            txt = requests.get(url=url, headers=header).json()
            if txt is '':
                break
            item = txt['data']["item"]
            for one in item:
                name = one["spname"]
                num = one["num"]
                info = name + " " + str(num) + "\n"
                f.write(info)
        time.sleep(0.5)
    f.close()
    print("招生计划已生成")