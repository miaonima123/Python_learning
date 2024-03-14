'''
列表
定义：由一系列特定顺序排列的元素组成。
使用：可以创建字母表中所有字母、数字0~9,、还可套用其他元素
Python中使用方括号[]表示，逗号分隔其中的元素

'''
# 示例
bickcles = ['trek','cannondale','redline','specialized']
print(bickcles)

# 1.访问列表元素
print(bickcles[0])         # trek
print(bickcles[0].title()) #花活 首字母大写

# 2.列表索引从0而不是1开始
# 如果需要访问列表最后一个元素，可以将索引改为-1 倒数第二-2以此类推
print(bickcles[-1])  # >>> specialized

# 3.花活玩法 使用列表中的值
message = f"My first bicycle was {bickcles[-2].title()}"
print(message)

# 4.修改列元素表
motorcyles = ['honda','yamaha','suzuki']
# motorcyles[0] = 'ducadi'
print(motorcyles)


# 5.列表队尾添加元素
# 方法 1
# append：.append() 默认在列表末尾追加新元素，不影响其他元素
motorcyles.append("ducadi")
print(motorcyles)
# 或者创建空列表再追加
motorcyles = []
motorcyles.append("honda")
motorcyles.append("yamaha")
motorcyles.append("suzuki")
print(motorcyles)

# 5.列表中插入元素
# 方法 2
# insert： .insert() 可在列表的任意位置添加新元素，剩下元素会往右移一个位置。
little_car = ['honda','suzuki',"hyundi"]
little_car.insert(0,"chery")
print(little_car)

# 6.列表删除元素
# 方法1 
# del : del() 如果知道要删除第几个可以用该语句
# 注意 不是方法 是函数  并且没有返回值
little_car = ['honda','suzuki',"hyundi"]
del(little_car[0])
print(little_car)

# 6. 列表删除元素
# 方法2
# pop(): .pop() 方法删除列表末尾的元素，并让你能够接着使用它。
# ()括号里 如果是正数 则按0从左侧找，负数从-1开始从右侧第一个找，如果不写则默认按末尾第一个元素，且会改变原列表
# 注：有返回值
little_car = ['honda','suzuki',"hyundi"]
my_car = little_car.pop(1)
print(little_car,my_car)

# 7.列表删除元素方法
# 方法3
# remove():.remove(xx) 方法 根据列表中的值相匹配
# 注意：但需注意该方法只删除第一个匹配项目如列表仍有删除项，则需使用循环,如果是使用变量来删除值则该变量值不会变，可继续使用
little_car = ['honda','suzuki',"hyundi","suzuki"]
print(little_car)
little_car.remove('suzuki')
print(little_car)



# 练习
# 1. 嘉宾名单 如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请那些人？请创建一个列表，其中包含至少三个你想邀请的人，然后使用这个列表打印消息，邀请这些人来与你共进晚餐。
dinner_list = ["tom","John","david"]
for i in range(3):
    print(f"those people to me enjoy dinner {dinner_list[i].title()}")



print("第二次提交")
print("第三次提交")
print("第四次提交")
print("git上操作第一次")
print("我测试一下")
















# 练习

# 1. 姓名 将一些朋友的姓名存储在一个列表中，并将其命名为names。依次访问该列表每个元素，从而将每个朋友姓名都打印出来。
names = ["Judy","John","Tom Hanks"]

# 2. 问候语 继续使用3.1中的列表，但不打印每个朋友的姓名，而是为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名
# for i in range(3):
#     print(f"This is my stupid frined his name is {names[i]}")

