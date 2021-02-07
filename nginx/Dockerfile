FROM nginx:1.17.1

WORKDIR /home/www
# 替换为国内源
# 老子国外服务器要什么国内源
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
COPY ./compose/production/nginx/sources.list /etc/apt/

RUN apt-get update && apt-get install -y --allow-unauthenticated certbot python-certbot-nginx
RUN rm /etc/nginx/conf.d/default.conf
