# FPA_NLP

## Описание
Приложение для оценки соответствия продаж скрипту с использованием видеопотока. Анализируется видео и проверяются определенные действия продавца в соответствии с заданным скриптом. Результаты анализа возвращаются в виде отчета.

## Репозиторий
GitHub: [https://github.com/EgorLozh/FPA_NLP](https://github.com/EgorLozh/FPA_NLP)

## Конфигурация
Для настройки приложения используйте файл `.env` с переменными окружения:

```dotenv
REBBIT_USER=rmuser
REBBIT_PASSWORD=rmpassword
REBBIT_HOST=rabbitmq
REBBIT_PORT=15672
AMQP_PORT=5672
REBBIT_CONSUME_QUEUE=consume_queue
REBBIT_PUBLISH_QUEUE=publish_queue

MODEL_NAME=Qwen/Qwen2.5-3B-Instruct
```
Переменная MODEL_NAME название модели Qwen, доступные модели на сайте https://huggingface.co/Qwen
Модель для распознования речи - vosk. Необходимую модель можно скачать с https://alphacephei.com/vosk/models

## Makefile Команды
Для запуска и управления приложением доступны следующие основные команды Makefile:

``` bash
make all # запустит оба контейнера (приложение и брокер сообщений).
make app # запустит только контейнер с приложением.
make down # остановит и удалит все контейнеры.
```


## Пример входного сообщения
Приложение ожидает входное сообщение в брокере в следующем формате:

``` json
{
  "type": "request",
  "data": {
    "id": "12345",
    "video": {
      "url": "https://drive.google.com/file/d/1cxeXHVLiXp1KySvxYWBhkuGmNZ6bupla/view?usp=sharing"
    },
    "actions": [
      {
        "text": "Продавец поздоровался",
        "weight": 10
      },
      {
        "text": "продавец смог назначить встречу",
        "weight": 50
      },
      {
        "text": "продавец обработал отказ клиента",
        "weight": 50
      },
      {
        "text": "продавец был вежливым",
        "weight": 30
      },
      {
        "text": "продавец попрощался",
        "weight": 10
      }
    ]
  }
}

```

## Пример сообщения от сервиса
Сервис возвращает сообщение в брокер в следующем формате:

``` json
{
  "type": "report",
  "data": {
    "request_id": "12345",
    "total_score": 50,
    "actions": [
      {
        "text": "Продавец поздоровался",
        "weight": 10,
        "check": false
      },
      {
        "text": "продавец смог продать акции",
        "weight": 50,
        "check": true
      },
      {
        "text": "продавец был вежливым",
        "weight": 30,
        "check": false
      },
      {
        "text": "продавец попрощался",
        "weight": 10,
        "check": false
      }
    ]
  }
}
```
