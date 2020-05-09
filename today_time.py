from datetime import datetime

dt=datetime.now() #创建一个datetime类对象
d = dt.strftime('%d')
a = dt.strftime('%A')
yb = dt.strftime('%B %Y')

print(a)
print(d)
print(yb)
