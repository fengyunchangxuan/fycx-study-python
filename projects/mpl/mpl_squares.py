# coding=utf-8

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
plt.plot(squares, linewidth=5)
plt.title('平方数', fontsize=30)
plt.xlabel('值', fontsize=14)
plt.ylabel('平方数', fontsize="14")
plt.show()
