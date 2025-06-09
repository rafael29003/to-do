# FastAPI Tasks Project

## Описание

Это учебный проект на FastAPI для работы с задачами (tasks). Реализованы CRUD-операции: добавление, получение, удаление, отметка задачи как выполненной.

## Используемые технологии

- **Python 3.11**
- **FastAPI** — современный асинхронный web-фреймворк
- **Uvicorn** — ASGI сервер для запуска FastAPI
- **SQLAlchemy** — ORM для работы с базой данных
- **SQLite** — простая встроенная база данных
- **Pydantic** — для валидации и сериализации данных
- **Docker** (опционально) — для контейнеризации приложения

## Структура проекта

- `main.py` — точка входа, инициализация FastAPI
- `Router.py` — роуты (эндпоинты) для работы с задачами
- `repo.py` — слой работы с базой данных (CRUD-операции)
- `database.py` — настройка подключения к базе и модели таблиц
- `shemas.py` — Pydantic-схемы для задач и ошибок
- `requirements.txt` — зависимости проекта
- `Dockerfile` — инструкция для сборки Docker-образа

## Как запустить

### 1. Без Docker (локально)

```bash
python -m venv venv
source venv/bin/activate  # или .venv\Scripts\activate для Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

Приложение будет доступно по адресу: http://127.0.0.1:8000
Документация Swagger UI: http://127.0.0.1:8000/docs

### 2. Через Docker

```bash
docker build -t fastapi-app .
docker run -d -p 80:80 --name fastapi-container fastapi-app
```

Приложение будет доступно по адресу: http://localhost/

## Основные эндпоинты

- `POST   /tasks` — добавить задачу
- `GET    /tasks` — получить все задачи
- `GET    /tasks/{task_id}` — получить задачу по ID
- `DELETE /tasks/{task_id}` — удалить задачу
- `PUT    /tasks/{task_id}/done` — отметить задачу как выполненную
- `GET    /tasks/count/col` — количество выполненных задач
- `DELETE /tasks/by-name/name` — удалить задачу по имени

## Примечания

- Для просмотра и редактирования базы данных SQLite можно использовать [DB Browser for SQLite](https://sqlitebrowser.org/).
- Для асинхронной работы с SQLite используется aiosqlite.

---

Если возникнут вопросы — см. код или обращайтесь! 