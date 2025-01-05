import requests
from PIL import Image
from PIL import Image, ImageDraw, ImageFont, ImageColor

# отправляем запрос с заголовками по нужному адресу
#req = requests.get("https://premier.one")
#считываем текст HTTL - документа
#s = req.text
#print(s)


# Изменение размера изображения
# Открываем изображение и получение информации о файле
# (можно использовать любой файл .jpg или .png).
img = Image.open('car.PNG')
print("Исходный размер:", img.size)
print(f"Width: {img.width}")
print(f"Height: {img.height}")
print(f"Filename: {img.filename}")
print(f"Format: {img.format}")
print(f"Mode: {img.mode}")

# Уменьшаем размер изображения в два раза.
new_size = img.resize((img.width // 2, img.height // 2))
#Сохраняем уменьшенное изображение в файл с именем new_car.jpg.
# Конвертация PNG в JPEG (прозрачность будет заменена белым фоном)
img = img.convert("RGB")  # Переключение в режим RGB, необходимый для JPEG
img.save('new_car.jpg', 'JPEG')
img.show()

# поворот на 90 градусов
img = Image.open("new_car.jpg")
img1 = img.rotate(90)
# сохраняем новое изображение
img1.save("new_car_1.jpg")
img1.show()
# делаем черно-белой картинку
img = Image.open("new_car.jpg")
img2 = img.convert('1')
img2.show()

# вставляем картинку в картинку
img = Image.open ("new_car.jpg")
img3 = Image.open('cat.jpg')
img.paste(img3)
img.paste(img3, (img.width//2, img.height//2))
img.save("cat_in_car.jpg")
img.show()


