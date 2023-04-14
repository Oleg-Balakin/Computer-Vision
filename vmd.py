import cv2

cam = cv2.VideoCapture(0)                                                           # трансляция с камеры, 0 – первая веб-камера в системе, 1 – вторая и т.д.

while cam.isOpened():
    ret, frame = cam.read()
    ret, new_fraim = cam.read()

    diff = cv2.absdiff(frame, new_fraim)                                            # переменная с разницей между пикселями кадров
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)                                   # преобразование разницы в серый цвет
    blur = cv2.GaussianBlur(gray, (5, 5), 0)                                        # сглаживание по Гауссу, высота и ширина 5, без отклонений
    _, threshold = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)                  # пороговое значение для фиксации изменений
    dilate = cv2.dilate(threshold, None, iterations=3)                              # фильтр для расширения изображения
    contours, _ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # поиск контуров изображения

    for c in contours:
        if cv2.contourArea(c) < 5000:                                               # вычисление площади контура
            continue
        x, y, w, h = cv2.boundingRect(c)                                            # определение правой верхней координаты, ширины и высоты контура
        cv2.rectangle(frame, (x, y), (x + w, y + y), (0, 255, 0), 2)                # метод рисует прямоугольник

    if cv2.waitKey(10) == 27:                                                       # открытое окно пока не нажата кнопка esc
        break
    cv2.imshow('Camera', frame)
