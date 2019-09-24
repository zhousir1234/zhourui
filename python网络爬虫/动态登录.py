from PIL import Image
#打开一个图片，把图片保存为Image对象
code_img =Image.open('2018.jpg')

code_img.save('c.png')
#把图片变亮 0：黑色 255：白色
def change(x):
    print(x)
    return x*1.5
codeimg2 =code_img.img.point(change)
codeimg2.save('d.png')