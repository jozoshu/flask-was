# Flask WAS

### 개발환경

- OS:
    - Mac on M1 (local)
  - CentOS 7 (production)
- Language:
    - Python 3.9.2
- Framework:
    - Flask 2.0
- Database:
    - PostgreSQL 12.7


# Environment

## 1.1 Set .env file

~~~bash
$> cp .env.sample .env
$> vim .env

#== Environment Variables ==#

# Env (local, development, production)
ENV=local
...
~~~

## 1.2 Set virtual environment

poetry 를 이용하여 라이브러리 관리
~~~bash
$> virtualenv venv -p python3.9
$> source venv/bin/activate
(venv) $> poetry install
~~~

## 1.3 Run~!

~~~bash
(venv) $> python main.py
~~~
