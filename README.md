# Описание
REST API сервис для работы с палитрами цветов.
Требования к методам сервиса: <br>
- Метод регистрации. Должен принимать имя, логин и пароль пользователя.
- Метод входа. Принимает логин и пароль пользователя и представляет токен доступа для пользователя
- Методы для работы с палитрами: получение коллекции палитр, получение палитры по идентификатору, создание палитры, изменение палитры, удаление палитры. Пользователь может работать только с его палитрами.
- Методы для работы с цветами: получение коллекции цветов по идентификатору палитры, получение цвета по идентификатору, создание цвета, изменение цвета, удаление цвета. Цвета существуют только в рамках палитр. Пользователь может работать только с его палитрами.

# Используемые технологии
- django rest framework
- postgres;
- docker, docker-compose.

# Запуск
```shell
docker compose up --build
```

# Пример работы
Документация доступна по эндпоинту /swagger

### Вход
Регистрация
![image](https://github.com/aovsybo/palete-colors-crud/assets/66824112/18749d80-a719-4256-a658-664222fa2a96)

Авторизация
![image](https://github.com/aovsybo/palete-colors-crud/assets/66824112/6a54c12c-3b25-43ff-9763-1670ac08df7c)

### Палитры
Создание
![image](https://github.com/aovsybo/palete-colors-crud/assets/66824112/29192a8f-2ac9-4aed-9344-0dc6a7778f5d)

Просмотр
![image](https://github.com/aovsybo/palete-colors-crud/assets/66824112/9fba4c7e-0e96-4af1-ade4-19888360d233)

Редактирование
![image](https://github.com/aovsybo/palete-colors-crud/assets/66824112/dcfc8723-22b1-4dbd-96da-40aa53e45584)

Удаление
![image](https://github.com/aovsybo/palete-colors-crud/assets/66824112/172b0bcb-0045-4204-9817-fba7473dafb5)


### Цвета 
Создание с присвоением названия цвета, полученного через API сервиса https://www.thecolorapi.com/
![image](https://github.com/aovsybo/palete-colors-crud/assets/66824112/01766309-a54d-4062-886c-ab3a1e443f19)

Просмотр цветов (только внутри данной палитры)
![image](https://github.com/aovsybo/palete-colors-crud/assets/66824112/f850e606-2ef4-4fa2-9c6d-51817eedb874)

Редактирование 
![image](https://github.com/aovsybo/palete-colors-crud/assets/66824112/a63f6826-ea24-4759-8869-a9d01b31ae69)

Удаление
![image](https://github.com/aovsybo/palete-colors-crud/assets/66824112/fab04921-36e1-4d73-b33f-461de861015d)

