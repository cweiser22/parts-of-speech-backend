FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./requirements/base.txt ./requirements/base.txt
RUN pip install -r requirements/base.txt

COPY ./app /app/app


