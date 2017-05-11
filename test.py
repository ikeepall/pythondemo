class Rectangle:
#属性
    l=5
    w=4
#方法
    def setRect(self):
        print("请输入长和宽")
        self.l = int(input("长："))
        self.w = int(input("宽："))
    def getRect(self):
        print("长是%d，宽是%d" % (self.l,self.w))
    def getArea(self):
        return self.l*self.w
x=Rectangle()

print(x.getArea())

# 哈哈哈
# 呸
