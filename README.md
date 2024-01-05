# Описание проекта

1. Загружается excel файл с временным рядом в формате как time_seria.xlsx
2. С помощью  модели, основанной на нейронных сетях (LSTM), прогнозируется значение на следующий период

Для обращения к модели используется запрос POST. В теле запроса передается путь к excel файлу.

Postman collection: https://api.postman.com/collections/32065544-abbc4526-0fc3-42f8-b957-7165ba254909?access_key=PMAT-01HJZTYX1KR3QB5E1BXVW0XWAT

## Старт проекта
Для запуска проекта необходимо в папке docker ввести следующую команду.
```shell
docker-compose -f docker-compose.dev.yml up -d 
```
