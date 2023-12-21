FROM python:3.9-alpine

WORKDIR /code

COPY ./backend/*.py /code/
COPY ./backend/requirements.txt /code/

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80" ]