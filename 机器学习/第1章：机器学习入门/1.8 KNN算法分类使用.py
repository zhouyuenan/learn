# 1.1 数据加载
from sklearn import datasets  # 数据集
from sklearn.neighbors import KNeighborsClassifier  # 分类
# train 训练数据 test 测试数据
from sklearn.model_selection import train_test_split

# X表示数据，y表示目标值
X,y = datasets.load_iris(return_X_y=True)
print(X)
print(y)

# 1.2 数据拆分
print(X.shape)
X_train, X_test, y_train, y_test = train_test_split(
    X,  # 拆分数据
    y,  # 拆分数据
    test_size=0.2,  # 拆分比例，测试数据20%， 故30个样本
    random_state=1024  # 固定了随机状态
)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 1.3 算法建模
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train) # 建模、训练、拟合

# 1.4 算法预测
y_ = model.predict(X_test)  # 预测值
print(y_)
print("保留测试数据，真实值是:\n", y_test)

# 准确率
print((y_ == y_test).mean())
print(model.score(X_test, y_test))
