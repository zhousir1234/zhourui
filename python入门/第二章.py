#1.输入直角三角形的两个直角边的长度a、b求c的长度
num1=float(input('请输入一条边的长'))
num2=float(input('请输入另外一条边的长'))
a=num1
b=num2
c=((a**2)+(b**2))**(1/2)
print('c的长度是',c)

#2. 编写一个程序，用于实现两个数的交换
num1=float(input('请输入一个数'))
num2=float(input('请输入另一个数'))
a=num1
b=num2
#使用3个变量
c=a
a=b
b=c
print('b的值为',b)
#使用两个变量
#使用两个变量的第一种方法
a = a+b   #取两个数的和
b = a-b   #然后a-b等于a然后赋值给b
a = a-b   #然后a-b等于b然后赋值给a，完成值的交换
#使用两个变量的第二种方法
a,b = b,a
