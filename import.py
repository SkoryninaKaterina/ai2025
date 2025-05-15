import cv2

# Завдання 3
# Відкрийте зображення data/lesson1/Lenna.png
# Створіть наступні зображення:
# #
# img = cv2.imread("data/lesson1/Lenna.png", cv2.IMREAD_GRAYSCALE)
# #
# #
# img[:20,:] = 0
# img[-20:,:] = 255
# #
# img[:, :20] = 0
# img[:, -20:] = 0
# cv2.imshow("img", img )
# cv2.waitKey(0)


#DZ
# import numpy as np
# img = cv2.imread("data/lesson1/Lenna.png", cv2.IMREAD_GRAYSCALE)
#
# mask = img > 128
# result = np.zeros_like(img)
# result[mask] = 255
#
# cv2.imshow('маска > 128', result)
# cv2.waitKey(0)


#2
import numpy as np

img = cv2.imread("data/lesson1/baboo.jpg")

result = np.zeros_like(img)

result[15:45, :] = img[15:45, :]

cv2.imshow("Тільки очі", result)
cv2.waitKey(0)



