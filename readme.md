# Test Task SilkwayTransit

Цель задания: импортировать данные из файла `schema.xlsx` и соотнести данные запчасти по кодам. Реализовать TreeView для узлов: `PJ350200000`, `PJ350150000`,
`PJ350170000`
## Getting started

Используйте `make`, чтобы упростить запуск проекта

```bash
make help
```

Получим такой ответ:

```bash
force-start          Run project with setted Postgres on local machine
help                 Show this help
start                Start project with compose
```

Для запуска проекта с помощью `docker-compose` используйте
```bash
make start
```

Для запуска проекта без `docker` и с работающим `Postgres` используйте:
```bash
make force-start
```

## After start

Для импорта всех данных, перейдите по эндпоинту:
```http
http://127.0.0.1:8000/import/
```

Для TreeView:
```http
http://127.0.0.1:8000/tree/
```

Для TreeView в виде JSON:
```http
http://127.0.0.1:8000/json-tree/
```

