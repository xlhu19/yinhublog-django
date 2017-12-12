#!/bin/bash

source ./env.sh
NAME="yinhublog"
SHELL_FOLDER=$(dirname $(readlink -f "$0"))
DJANGODIR=${SHELL_FOLDER} #Django project directory
SOCKFILE=${SHELL_FOLDER}/run/gunicorn.sock # we will communicte using this unix socket
USER=root # the user to run as
GROUP=root # the group to run as
NUM_WORKERS=2 # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=DjangoBlog.settings # which settings file should Django use
DJANGO_WSGI_MODULE=DjangoBlog.wsgi # WSGI module name

echo "Starting $NAME as `whoami`"

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# --bind=unix:$SOCKFILE \
exec gunicorn  ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
--bind=0.0.0.0:8082 \
--log-level=error \
--log-file=-

