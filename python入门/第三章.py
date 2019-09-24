var=1
while var==1:
    name=(input("请输入一个名字"))
    print("你输入的名字是：",name)
print("good bye!")

for i in range(1,4):
     print(i)

i=1
#定义一个变量sum为0，用来存放和
sum=0
while i<=100:
	#每次sum和i相加
	if i%2==0:
		sum+=i
	i+=1
#执行完之后，打印sum的值
print("1-100之间偶数和是%d"%sum)