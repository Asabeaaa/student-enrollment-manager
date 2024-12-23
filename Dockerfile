FROM python:3.11.4-bullseye

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./src /code/src


EXPOSE 8000


CMD ["python3", "src/main.py"]

