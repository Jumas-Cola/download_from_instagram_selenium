downl_from_inst ![Python 3.6](https://pp.userapi.com/c846523/v846523407/b716d/N3RXKWFcPS0.jpg)
======
**downl_from_inst** – скрипт на Python для скачивания файлов из Инстаграм (instagram.com)

Usage: py_inst_img.py <***user***> <***count_imgs***> <***login***> <***password***>

Обязательные параметры
------------
* <***user***> - https://www.instagram.com/<***user***>/

Опциональные параметры
------------
* <***count_imgs***> - количество изображений, которое надо скачать. Не менее 12 (если указать меньше - всё равно скачает 12. По умолчанию - 9999).
* <***login***> - логин для авторизации в Инстаграм (некоторые аккаунты могут просматривать только авторизованные пользователи).
* <***password***> - пароль для авторизации в Инстаграм (некоторые аккаунты могут просматривать только авторизованные пользователи).

```python
python3 downl_from_inst.py _ierathel_ 15 login password

```

Библиотека instagram
------------
В работе скрипт использует библиотеку instagram.py  
Подробнее о библиотеке здесь:
[https://habr.com/post/339620/](https://habr.com/post/339620/)

geckodriver
------------
Geckodriver – это адаптер, преобразователь из протокола W3C WebDriver в протокол Marionette.
Marionette – это название протокола и встроенного в браузер сервера для удалённой отладки.   
Подробнее о geckodriver здесь:
[http://barancev.github.io/geckodriver/](http://barancev.github.io/geckodriver/)
  
Свежий geckodriver можно найти здесь:
[https://github.com/mozilla/geckodriver/releases/](https://github.com/mozilla/geckodriver/releases/)
