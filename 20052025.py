import cv2
#
# img = cv2.imread("data/lesson/castello_noised.png")
#
# kernel = np.array([[0.05, 0.1, 0.05],
#                    [0.1, 0.4, 0.1],
#                    [0.05, 0.1, 0.05]])
#
# new_img = cv2.filter2D(img,#оигінальне зображення
#                        -1, #згортка для кожного кольору
#                        kernel)#ядро з коєфіцієнтами
# cv2.imshow('result', new_img)
#
#
# #гаусове розмиття
# new_img1 = cv2.GaussianBlur(img,
#                            ksize=(3, 3),
#                            sigmax=10
#                            )
#
#
#
# cv2.imshow("result", img)
# cv2.waitKey(0)


# Завдання 1
# Відкрийте зображення data/lesson4/digit_noised.png.
# Виконайте наступні дії
#  Проведіть бінарізацію(можливо з попереднім
# видаленням шуму)
#  Застосуйте морфологічні оператори для покращення
# результату


img = cv2.imread("itstep-ai/data/lesson4/digit_noised.png")

g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(g_img, (3,3), sigmaX= 0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))


erode = cv2.erode(blur, kernel, iterations=2)
mask = erode > 30

erode[mask] = 255
erode[~mask] = 0
# adapt_img = cv2.adaptiveThreshold(blur, 255,
#                                   cv2.ADAPTIVE_THRESH_MEAN_C,
#                                   cv2.THRESH_BINARY, 7,
#                                   0.3)




cv2.imshow('res', img)
cv2.imshow('g_img', g_img)
cv2.imshow('blur', blur)
cv2.imshow('erode', erode)


#cv2.imshow('adapt_img', adapt_img)
cv2.waitKey(0)