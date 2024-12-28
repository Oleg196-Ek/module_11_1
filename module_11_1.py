import requests
from PIL import Image
import os, sys

# отправляем запрос с заголовками по нужному адресу
#req = requests.get("https://premier.one")
#считываем текст HTTL - документа
#s = req.text
#print(s)


im = Image.open('img.png')
print(im.format, im.size, im.mode)#использую атрибуты экземпляра для просмотра содержимого файла
im.show()# показ рисунка


imag = Image.open('66263.jpg')
print(imag.format, imag.size, imag.mode)
imag.show()




