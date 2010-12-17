#!/bin/sh

cd `dirname $0`

PWD=`pwd`
BASEPATH=`basename $PWD`
PYTHON=python
SCREEN=screen
ENVDIR=env

if [ -d $ENVDIR ]; then
    echo 'Using python from virtualenv environment' >&2
    PYTHON=$ENVDIR/bin/python
fi

if [ ! -f portnumber ]; then
    echo 'No port number set!' >&2
    echo 'Please create a file named "portnumber" in the current directory with' >&2
    echo 'a locally unique portnumber in it, like "1234".' >&2
    exit 1
fi

if [ $1 ]; then
    $PYTHON manage.py $*
else
    $SCREEN -S $BASEPATH $PYTHON manage.py runserver `hostname`:`cat portnumber`
fi

