age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
	print("请输入正确的年龄。")
elif age == 1:
	print("相当于 14 岁的人。")
elif age == 2:
	print("相当于 22 岁的人。")
elif age > 2:
	human = 22 + (age -2)*5
	print("对应人类年龄: ", human)
	
### test 
a = 1000000
b = "-"
print("{0:{2}^{1},}\n{0:{2}>{1},}\n{0:{2}<{1},}".format(a,30,b))

### 退出提示，本地环境下可以使用这样的退出提示使代码更易用
input('点击 enter 键退出')
