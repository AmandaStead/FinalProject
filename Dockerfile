FROM python:3.8


WORKDIR /app


COPY . .

ADD Movies.py .
ADD Receipt.py .


RUN python -m pip install --upgrade pip
RUN pip install wheel
RUN pip install flask

EXPOSE 8000




