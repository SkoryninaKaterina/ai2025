# import cv2
# #
# # img = cv2.imread("data/lesson/castello_noised.png")
# #
# # kernel = np.array([[0.05, 0.1, 0.05],
# #                    [0.1, 0.4, 0.1],
# #                    [0.05, 0.1, 0.05]])
# #
# # new_img = cv2.filter2D(img,#оигінальне зображення
# #                        -1, #згортка для кожного кольору
# #                        kernel)#ядро з коєфіцієнтами
# # cv2.imshow('result', new_img)
# #
# #
# # #гаусове розмиття
# # new_img1 = cv2.GaussianBlur(img,
# #                            ksize=(3, 3),
# #                            sigmax=10
# #                            )
# #
# #
# #
# # cv2.imshow("result", img)
# # cv2.waitKey(0)
#
#
# # Завдання 1
# # Відкрийте зображення data/lesson4/digit_noised.png.
# # Виконайте наступні дії
# #  Проведіть бінарізацію(можливо з попереднім
# # видаленням шуму)
# #  Застосуйте морфологічні оператори для покращення
# # результату
#
#
# img = cv2.imread("itstep-ai/data/lesson4/digit_noised.png")
#
# g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# blur = cv2.GaussianBlur(g_img, (3,3), sigmaX= 0)
#
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
#
#
# erode = cv2.erode(blur, kernel, iterations=2)
# mask = erode > 30
#
# erode[mask] = 255
# erode[~mask] = 0
# # adapt_img = cv2.adaptiveThreshold(blur, 255,
# #                                   cv2.ADAPTIVE_THRESH_MEAN_C,
# #                                   cv2.THRESH_BINARY, 7,
# #                                   0.3)
#
#
#
#
# cv2.imshow('res', img)
# cv2.imshow('g_img', g_img)
# cv2.imshow('blur', blur)
# cv2.imshow('erode', erode)
#
#
# #cv2.imshow('adapt_img', adapt_img)
# cv2.waitKey(0)

#
# Завдання 1
# Відкрийте зображення data/lesson2/darken.png
# Переведіть його в формат HSV
# Далі для каналу value зробіть одну з двох обробок
# 1. Застосуйте вирівнювання гістограм
# 2. Збільшіть значення десь на 20-50%, для цього
# o Помножте усі значення value на відповідне
# число
# o Оскільки ви вийдете за межі діапазону 0-255
# застосуйте
# np.clip(value, 0, 255)
# o Оскільки результат не ціле число
# value.astype(np.unit8)
# o Напишіть для цієї частини функцію з
# utils.trackbar_decorator
# Переведіть результат назад у формат BGR
# Виведіть результат для двох варіантів обробоки


# Завдання 1
# Виведіть відео з файлу data\lesson7\text.mp4 на екран та
# збережіть в новий файл.
# Змініть розмір зображення.
# Завдання 2
# Відкрийте відео з файлу data\lesson7\text.mp4. Проведіть
# бінарізацію кадрів та збережіть в новий файл.



# import cv2


cap = cv2.VideoCapture(r'data\lesson7\text.mp4')
# ret, img = cap.read()
# if not ret:
#     print("Не вдалося відкрити відео.")
#
# cv2.imshow("frame", img)
# cv2.waitKey(5000)
#
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))# Встановлення FPS
# print(width, height)
# writer = cv2.VideoWriter('data/lesson7/output.mp4',
#                           cv2.VideoWriter_fourcc(*'mp4v'),
#                           30,  # FPS
#                           (width, height)  # Розмір кадру
#                           )
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     # # Зміна розміру кадру
#     resized_frame = cv2.resize(frame, None, fx=0.3, fy=0.3)
#
#     # Відображення кадру
#     cv2.imshow("Resized Frame", resized_frame)
#
#     writer.write(resized_frame)  # Запис кадру у відео
#
#     # Вихід з циклу при натисканні клавіші 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# writer.release()