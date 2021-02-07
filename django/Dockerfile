FROM python:3.6.3
WORKDIR /src
COPY . .
RUN pip3 install -r requirements.txt \
&& pip3 install gunicorn

CMD ["gunicorn","-c","./django/gunicorn.py","qaschool.wsgi"]