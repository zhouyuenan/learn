import re
# (1) . 通配符、万能通配符或通配元字符，匹配1个除了换行符\n以外任何符号
s = "apple ape agree age amaze animate advertise a\ne"
ret = re.findall("a.e", s)
print(ret)