TEST CASE STRIPER

Для запуска используеться Python 3.11, Django 5.0 или docker-compose.
Перед запуском создать файл .env и прописать следующие параметры:

1) debug=1  # Программа настроена на Debug=1, не меняем.
2) secret_key=""    # Секретный ключ Django приложения
3) allowed_hosts=localhost,127.0.0.1    # хосты через запятую
4) STRIPE_SECRET_KEY='' # Секретный ключ striper
5) STRIPE_PUBLISHABLE_KEY=''    # Публичный ключ striper


Задача:
 	Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
1) 	Django Модель Item с полями (name, description, price)
2) 	API с двумя методами:
2.1) 	GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item.
        При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться
        запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
2.2) 	GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет
        информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос
        на /buy/{id}, получение session_id и далее с помощью JS библиотеки Stripe происходить редирект на
        Checkout форму stripe.redirectToCheckout(sessionId=session_id)

Бонусные задачи:
3) 	Запуск используя Docker
4) 	Использование environment variables
5) 	Просмотр Django Моделей в Django Admin панели
6) 	Запуск приложения на удаленном сервере, доступном для тестирования
7) 	Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое
 	Order c общей стоимостью всех Items
8) 	Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами
 	при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме.
9) 	Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты
 	выбранного товара предлагать оплату в соответствующей валюте
10) Реализовать не Stripe Session, а Stripe Payment Intent.
