# Сайт для небольшого кафе/ресторана

### Описание
Проект выполнен на фреймворке Django с использованием бесплатного шаблона и представляет собой 3-страничный адаптивный сайт со слайдером на главной странице.
Для наглядности присутствует база данных с внесенными тестовыми данными.

Вид главной страницы сайта:

![Главная](https://github.com/user-attachments/assets/40d9bd51-5c17-4a7e-b8a3-d77b7c7e9103)

*Внимание! Изображения слайдера не отображаются в браузере Mozilla Firefox!*


На странице "Меню" в зависимости от выбранной категории (завтрак/обед/ужин) выводятся соответствующие последние 6 блюд, полученные из БД в результате сортировки случайным образом:

![Меню](https://github.com/user-attachments/assets/b1244616-4eda-4cfd-897a-c44479f7b98b)



Страница "Контакты" содержит подключенную Яндекс.Карту и форму обратной связи (с валидацией полей ввода):

![Контакты](https://github.com/user-attachments/assets/5ca64465-7307-48a9-9134-e65eba5bc076)



Отправка письма с формы обратной связи для наглядности производится в консоль (можно изменить в настройках проекта):

![Консоль](https://github.com/user-attachments/assets/43ce0fdf-fa71-42db-aa7c-1ff0f6d2a2e4)



Особенностью административной области сайта является показ изображений блюд:

![Админка](https://github.com/user-attachments/assets/a7f0e353-2d65-4e07-98ba-c6a03e7d68da)

---
### Инструкция по сборке и запуску проекта
1. Скачать и установить интерпретатор Python - https://www.python.org/downloads/

    Далее выполнить следующие команды в консоли:

2. **cd <имя_каталога>**    # Перейти в каталог где будет проект
3. **git clone https://github.com/stankv/Django_Restaurant.git**    # Клонировать репозиторий
4. **cd Django_Restaurant**    # Перейти в каталог проекта
5. **pip install -r requirements.txt**    # Установить пакеты и зависимости
6. **python manage.py runserver**    # Запустить локальный сервер

Сайт будет доступен локально по адресу http://127.0.0.1:8000/. 

Админка - по адресу http://127.0.0.1:8000/admin/.

Вход в админку: login: **admin**, password: **1234**