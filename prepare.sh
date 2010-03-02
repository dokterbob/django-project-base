#!/bin/sh

PWD=`dirname $0`
BASEPATH=`basename $PWD`

BASH=bash
GIT=git

if [ -d .git ]; then
    echo 'Checkout out submodule dependencies'
    $GIT submodule init
    $GIT submodule update
    if [ $? != 0 ]; then
        echo 'Error updating submodules.'
        exit -1
    fi
fi

if [ ! -f portnumber ]; then
    echo 'Port number not set.'
    while [ -z "$PORTNUMBER"  ]; do
        read -p 'Which port number should the builtin server listen to? ' -e PORTNUMBER
        echo
        echo "Setting default port number to: $PORTNUMBER"
        echo
    done
    
    echo $PORTNUMBER > portnumber
fi

if [ ! -f settings_local.py ]; then
    echo 'No local settings file found.'
    cp -v settings_local.py.example settings_local.py
    
    echo
    echo 'Generating secret key in settings_local.py.'
    SECRET_KEY=`./runserver.sh generate_secret_key`
    echo >> settings_local.py
    echo "# Make this unique, and don't share it with anybody." >> settings_local.py
    echo "SECRET_KEY = '$SECRET_KEY'" >> settings_local.py
fi

if [ ! -f database.sqlite ]; then
    echo 'No database found, running syncdb.'
    $BASH runserver.sh syncdb
fi
