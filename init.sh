#!/bin/bash

export CURRENT_DIR=`pwd`

##### SYSTEM ######

sudo apt-get update;
sudo apt-get upgrade;
sudo apt-get install mysql-client mysql-server libmysqlclient-dev nginx libevent-dev libpq-dev libncurses5-dev memcached
sudo apt-get install zsh libzmq1 libzmq-dev make automake bison build-essential python-dev python-mysqldb python-virtualenv openssl libssl-dev libevent-dev

sudo apt-get install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev

#We should fix PIL path libraries by: (use x86_64-linux-gnu OR i386-linux-gnu as per architecture)
sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib

#If you want to install webserver with nginx
#sed "s#<static_content_path>#$CURRENT_DIR#g" conf/template_nginx.conf > conf/ignore_nginx.conf
#sudo ln -s -t /etc/nginx/sites-enabled/ $CURRENT_DIR/conf/ignore_static_nginx.conf
#sudo /etc/init.d/nginx restart

#If you want to install system wide oh-my-zsh
#curl -L https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh | sh
#chsh -s /bin/zsh

##################

virtualenv envproj
source envproj/bin/activate

export PREFIX=$CURRENT_DIR/envproj/

pip install -r requirements.txt

cd $CURRENT_DIR
mkdir logs
cd logs
mkdir project supervisord
cd $CURRENT_DIR
