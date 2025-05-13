import cv2

# Завдання 3
# Відкрийте зображення data/lesson1/Lenna.png
# Створіть наступні зображення:

img = cv2.imread("data/lesson1/Lenna.png", cv2.IMREAD_GRAYSCALE)


# img[:20,:] = 0
# img[-20:,:] = 255

img[:, :20] = 0
img[:, -20:] = 0
cv2.imshow("img", img )
cv2.waitKey(0)


