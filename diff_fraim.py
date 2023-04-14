import cv2


def diffImg(f0, f1, f2):              # функция возвращает разницу между массивами кадров
    d1 = cv2.absdiff(f2, f1)          # переменная с абсолютной разницей между массивами (кадрами)
    d2 = cv2.absdiff(f1, f0)          # переменная с абсолютной разницей между массивами (кадрами)
    return cv2.bitwise_and(d1, d2)

cam = cv2.VideoCapture(0)             # трансляция с камеры, 0 – первая веб-камера в системе, 1 – вторая и т.д.

winName = 'Motion Detector'                      # название окна
cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)    # функция создает окно для видео c параметрами,
                                                 # WINDOW_AUTOSIZE – автоматически устанавливает размер окна
                                                 # WINDOW_NORMAL – позволяет вручную изменять размер окна
                                                 # WINDOW_FULLSCREEN – изменяет размер окна на полноэкранный
f1 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)   # кадры преобразованные в оттенки серого
f0 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
f2 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

while True:
    cv2.imshow(winName, diffImg(f1, f0, f2))

    f1 = f0
    f0 = f2
    f2 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyWindow(winName)
        break
