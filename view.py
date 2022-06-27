import matplotlib.pyplot as plt
import matplotlib

"""2019 理科
本科一批A段 507
本科一批B段 507
本科二批A段 447
本科二批B段 434
2020 理科
本科一批A段 537
本科二批A段 473
本科二批B段 453
2021 理科
本科一批A段 505
本科二批A段 446
本科二批B段 431
"""
plt.rcParams['font.sans-serif']=['SimHei']
x=["2019","2020","2021"]
y=[507,537,505]

plt.plot(x, y, "g", marker='D', markersize=5)
plt.xlabel("年份")
plt.ylabel("录取分数")
plt.title("2019至2020年录取分数线")
plt.show()