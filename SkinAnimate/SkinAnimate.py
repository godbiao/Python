#  样式对象
class AnimStyle:
    def __init__(self, sid):
        self.sid = sid
        self.extra_list = []

    def add_extra(self, extra):
        self.extra_list.append(extra)

    def __str__(self):
        return '[%s]\nextra=%s' % (self.sid, ','.join(self.extra_list))


# 动画对象
class SimpleAnimate:
    def __init__(self, animate_type):
        self.index = ""
        self.animate_type = animate_type

    def __str__(self):
        return '[Extra%s]\nType=%s' % (self.index, self.animate_type)


# 创建一个动画对象
extra1 = SimpleAnimate('1')
extra1.index = '701'
print(extra1)

# 创建大背景样式对象
bg = AnimStyle('201')

# 向大背景中添加对象
bg.add_extra(extra1.index)


print(bg)
