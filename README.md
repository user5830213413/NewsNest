# News Nest

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Student)](https://git.io/typing-svg)

Этот проект представляет собой веб-приложение для добавления, редактирования и удаления новостей.

## ⚙️ Стэк технологий:

**Frontend:**

- [Vue 3 (composition api)](https://v3.ru.vuejs.org/)
- [Vue Router](https://v3.router.vuejs.org/)
- [Axios](https://ru.vuejs.org/v2/cookbook/using-axios-to-consume-apis)
- [TailwindCSS](https://tailwindcss.com/)

**Backend**

- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)

## Как запустить?

**Backend**

```sh
cd backend
cd app
pip install -r requirements.txt
python main.py
```

**Frontend**

```sh
cd frontend
cd vue-project
npm install
npm run dev
```

## Функциональные возможности:

- **Авторизация** - Пользователи могут авторизоваться в системе для получения доступа к управлению новостями.

- **Добавление новостей** - Зарегистрированные пользователи могут добавлять свои новости через удобный интерфейс.

- **Редактирование новостей** - Пользователи имеют возможность редактировать свои собственные новости для обновления информации.

- **Удаление новостей** - У каждого пользователя есть право удалить свои новости по необходимости.
