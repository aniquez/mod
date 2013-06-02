#!/bin/sh

PYTHONPATH="."
WORKERS=5
PROJECT=`echo ${PWD##*/}`
PWD=`pwd`
PID="logs/gunicorn.pid"
RETVAL=0
DEBUG=`python -c "from base import settings; print settings.DEBUG"`

if [ "$DEBUG" = "True" ]; then
    echo "Debug is True. Start production server with Debug=False."
    exit
fi

start()
{
    echo "Starting Server for project $PROJECT"
    gunicorn_django -c confs/gunicorn_conf.py
}

stop()
{
    echo "Stopping $PROJECT"
    kill -QUIT `cat $PID` && echo "OK" || echo "failed";
}

reload()
{
    echo "Reloading $PROJECT"
    if [ -f $PID ]
    then kill -HUP `cat $PID` && echo "OK" || echo "failed";
    fi
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        reload
        ;;
    reload)
        reload
        ;;
    force-reload)
        stop && start
        ;;
    *)
        echo $"Usage: $0 {start|stop|restart}"
        RETVAL=1
esac
exit $RETVAL
