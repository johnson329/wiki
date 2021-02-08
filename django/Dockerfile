FROM python:3.6.3
WORKDIR /src
COPY . .
RUN pip3 install -r requirements.txt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com\
&& pip3 install gunicorn
#&& python3 manage.py migrate

#CMD ["gunicorn","-c","./django/gunicorn.py","qaschool.wsgi"]
RUN chmod a+x boot.sh
ENTRYPOINT ["./boot.sh"]
