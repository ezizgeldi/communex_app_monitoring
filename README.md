# communex_app_monitoring
Monitoring of remote servers on flask


Для сбора метрик CPU и RAM с удаленных серверов и вывода их на график с использованием Flask, мы можем реализовать следующий подход:


1 Сбор данных с удаленных серверов:
      Используем библиотеку psutil для получения метрик CPU и RAM

2 Централизованный сбор данных с использованием Flask:

3 Визуализация данных:
      Используем библиотеку matplotlib или plotly для построения графиков.



metrics_app.py - Скрипт для получения метрик на удаленном сервере который будет возвращать метрики CPU и RAM.

central_server.py - Централизованный сбор данных с использованием Flask которое будет опрашивать удаленные сервера и сохранять данные.

data_visualization.py - Создаем маршрут для отображения графиков с использованием библиотеки plotly

index.html -  Шаблон  для отображения
