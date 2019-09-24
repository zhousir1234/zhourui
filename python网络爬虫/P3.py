import pytesseract
from PIL import Image
#将图像文件转换成image实列
image = Image.open('test.jpg')
#将图像中的文本转换成文本，进行输出
text = pytesseract.image_to_string(image)
print(text)