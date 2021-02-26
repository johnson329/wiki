#!/bin/bash

# backup database by exporting db as a single sql file

# change the host, user, db if necessary:
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_DB=wiki
M_P=

# backup file name:
BACKUP=wiki-`date +"%Y-%m-%d_%H_%M_%S"`.sql

echo "mysqldump -h $MYSQL_HOST --opt --hex-blob --set-gtid-purged=OFF --user $MYSQL_USER -p$M_P $MYSQL_DB > $BACKUP"

mysqldump -h $MYSQL_HOST --opt --hex-blob --set-gtid-purged=OFF --user $MYSQL_USER -p$M_P $MYSQL_DB > $BACKUP

gzip $BACKUP

echo "backup ok: $BACKUP.gz"