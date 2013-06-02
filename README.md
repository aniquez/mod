# README #


# Install dependencies and virtual environment #
Get the base project via Git
run  init.sh using
    $ ./init.sh   or
    $ bash init.sh

#Django-South Basics

After creating the model first time
> python manage.py schemamigration appname --initial

To apply the migration first time, first do syncdb then do:
> python manage.py migrate appname

If you have done syncdb, or want to skip a migration
> python manage.py migrate appname 0001 --fake

To create migration after changing model
> ./manage.py schemamigration appname --auto

To apply un-applied migrations to db
> python manage.py migrate appname

Facing issues with PIL, pkg_resources
curl http://python-distribute.org/distribute_setup.py | python

#For PIL jpg and other support  :
 sudo apt-get install libjpeg libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev

 The following might be different depending on your machine
 ln -s /usr/lib/`uname -i`-linux-gnu/libfreetype.so /usr/lib/
 ln -s /usr/lib/`uname -i`-linux-gnu/libjpeg.so /usr/lib/
 ln -s /usr/lib/`uname -i`-linux-gnu/libz.so /usr/lib/
 pip install -U PIL:
