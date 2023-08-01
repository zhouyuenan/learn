# ------------------------------------------------
# Program:
#       This program is used to learn python grammar.
#       此脚本用于学习python语法
# History:
#       2023/05/21 周月南 First release
# ------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0.05, 10, 1000)
y = np.cos(x)
plt.plot(x, y, ls="-", lw=2, label="plot figure")
plt.legend()
plt.show()