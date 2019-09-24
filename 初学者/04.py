#条件分支
import random
secret = random.randint(5,7)
print('----小天使的数字----')
temp=input('猜一猜我心里的数字是什么：')
guess = int(temp)
while guess!=secret:
    temp=input('哎呀，猜错了，请重新输入吧：')
    guess = int(temp)
    if guess==secret:
        print("猜对了啦")
        print("猜对了也没奖励")
    elif guess>secret:
        print("大了大了，弟弟")
    elif guess<secret:
        print("小了小了，弟弟")

print("游戏结束，不跟你玩了")
