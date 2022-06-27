import requests
import time


def get_num(school_id):
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 "
                      "Safari/537.36 Edg/101.0.1210.39 "
    }
    dt = {2: "文科", 1: "理科"}
    for j in dt.keys():
        for i in range(2019, 2022):
            url = "https://static-data.gaokao.cn/www/2.0/schoolprovinceindex/{}/{}/14/{}/1.json".format(i,school_id,j)
            txt = requests.get(url=url, headers=header, ).json()
            item = txt['data']["item"]
            print(item[0]["year"],dt[j])
            for one in item:
                print(one["local_batch_name"], one["min"])
            time.sleep(0.5)


if __name__ == '__main__':
    get_num(269)
