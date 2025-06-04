# FAST-AF

**fast-af** is a FastAPI project generator designed to help developers quickly scaffold backend applications
**forked from [Peter Akande's Fast Template Python](https://github.com/PeterAkande/fast-template-python)** 

## Installation
(not published yet)

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

To initialize a project, in the existing root folder:

```sh
fast-af sm <project_name>
```


Once the template is set up, you'll need to navigate to your `.env` file as required by the `settings.py` file (modify the values specified to suit your enviroment, currently postgres, redis, and google credentials are required)
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
