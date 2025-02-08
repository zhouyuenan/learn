import re

string1 = "rain yuan eric 张三"

print(string1.find("yuan"))

string2 = "rain 12 yuan 34 eric 556 张三 7892"
ret = re.findall("\d+", string2)
print(ret)