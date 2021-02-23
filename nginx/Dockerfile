FROM nginx:1.17.1

WORKDIR /home/www
# 替换为国内源
# 老子国外服务器要什么国内源
#RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
#COPY ./nginx/sources.list /etc/apt/
#certbot --nginx
RUN apt-get update && apt-get install -y --allow-unauthenticated certbot python-certbot-nginx
RUN rm /etc/nginx/conf.d/default.conf

#IMPORTANT NOTES:
# - Congratulations! Your certificate and chain have been saved at:
#   /etc/letsencrypt/live/v2nwork.com/fullchain.pem
#   Your key file has been saved at:
#   /etc/letsencrypt/live/v2nwork.com/privkey.pem
#   Your cert will expire on 2021-05-24. To obtain a new or tweaked
#   version of this certificate in the future, simply run certbot again
#   with the "certonly" option. To non-interactively renew *all* of
#   your certificates, run "certbot renew"
# - Your account credentials have been saved in your Certbot
#   configuration directory at /etc/letsencrypt. You should make a
#   secure backup of this folder now. This configuration directory will
#   also contain certificates and private keys obtained by Certbot so
#   making regular backups of this folder is ideal.
# - If you like Certbot, please consider supporting our work by:
#
#   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
#   Donating to EFF:                    https://eff.org/donate-le

