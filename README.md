# FAST-AF

**FAST-AF** is a FastAPI project generator designed to help developers quickly scaffold backend applications with varying levels of complexity. It provides three template options: **lightweight (sm)**, **standard (md)**, and **full-stack (lg)**, catering to different project needs and developer expertise.

This project is **forked from [Peter Akande's Fast Template Python](https://github.com/PeterAkande/fast-template-python)** 

---

## Features

### Template Options
(future)
1. **Lightweight (sm)**:
project_name
├── routers
│   ├── auth_router.py
│   ├── crud_router.py
├── root
│   ├── app.py
│   ├── database.py
│   ├── settings.py
├── schemas
│   ├── auth_schemas.py
│   ├── crud_schemas.py
├── .env
├── requirements.txt
2. **Standard (md)**:
3. **Full-Stack (lg)**:


---

## Installation
(not implemented)

You can install FAST-AF via `pip`:

```sh
pip install fast-af
```

Or using `poetry`:

```sh
poetry add fast-af
```

---

## Usage

To initialize a project, in an existing root folder:

```sh
fast-af sm .
```


Once the template is set up, you'll need to create a `.env` file as required by the `settings.py` file (feel free to modify it to suit your needs).
An example of a `.env` is:
```
POSTGRES_URL = postgresql+asyncpg://postgres@localhost/your_db_name

ACCESS_TOKEN_SECRET = Your-Access-Token-Secret
REFRESH_TOKEN_SECRET = Your-Refresh-Token-Secret
RESET_PASSWORD_SECRET = Your-Reset-Password-Secret

SECRET_KEY = Your-Secret-Key

JWT_ALGORITHM = HS256

MAIL_USERNAME = yourname@yourmail.com
MAIL_FROM_NAME = Your-Name
MAIL_PASSWORD = yourmailpassword
MAIL_FROM = yourname@yourmail.com
MAIL_PORT = 000 # 587 for gmail
MAIL_SERVER = your_mail_server # smtp.gmail.com for gmail

REDIS_HOST = localhost
REDIS_PORT = 6379

GOOGLE_CLIENT_ID = YOUR_GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET = YOUR_GOOGLE_CLIENT_SECRET
GOOGLE_REDIRECT_URI = https://yourdomain.com/auth/google/callback
```
