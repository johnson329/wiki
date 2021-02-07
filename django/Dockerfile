FROM python:3.6.3
WORKDIR /src
COPY . .
RUN pip3 install -r requirements.txt -i http://pypi.douban.com/simple \
&& pip3 install gunicorn

CMD ["gunicorn","-c","./django/gunicorn.py","qaschool.wsgi"]