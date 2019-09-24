from random import randint
import pytesseract
from PIL import Image

#随机获取一个本地验证码图片中的名称
picName = str(randint(0,9)) + '.png'
#加载图片
image = Image.open('image/' + picName)
#从图片中识别验证码
text = pytesseract.image_to_string(image)
#输出图片名称和识别到的验证码文字
print(picName+":"+text)