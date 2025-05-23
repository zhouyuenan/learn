# 2.1 加载数据拆分
from sklearn import datasets  # 数据集
from sklearn.neighbors import KNeighborsClassifier  # 分类
from sklearn.model_selection import train_test_split

# X表示数据，y表示目标值
X, y = datasets.load_iris(return_X_y=True)
print(X)
print(y)
# train 训练数据 test 测试数据
