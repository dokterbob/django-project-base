#!/bin/sh

PWD=`dirname $0`
BASEPATH=`basename $PWD`
PYTHON=python
SCREEN=screen

cd $PWD

if [ ! -f portnumber ]; then
    echo 'No port number set!' >&2
    echo 'Please create a file named "portnumber" in the current directory with' >&2
    echo 'a locally unique portnumber in it, like "1234".' >&2
    exit -1
fi

if [[ $1 != "" ]]; then
    $PYTHON manage.py $*
else
    $SCREEN -S $BASEPATH $PYTHON manage.py runserver_plus `hostname`:`cat portnumber`
fi

