import requests
from PIL import Image
import os, sys

# отправляем запрос с заголовками по нужному адресу
#req = requests.get("https://premier.one")
#считываем текст HTTL - документа
#s = req.text
#print(s)

im = Image.open('img.png')
im.save('cat.jpg')# Преобразуем изображение из одного формата в другой.
im = Image.open('cat.jpg')
im.thumbnail((400,200))# изменяем размеры рисунка
im.save('cat_thumbnail.jpg')
im = Image.open('cat.jpg')
im.transpose(Image.FLIP_TOP_BOTTOM)
im.save('cat_flip.jpg')

print(im.format, im.size, im.mode)#использую атрибуты экземпляра для просмотра содержимого файла
im.show()# показ рисунка




