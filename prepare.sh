#!/bin/sh

# Go to current directory
cd `dirname $0`

PWD=`pwd`
BASEPATH=`basename $PWD`

GIT=git
VIRTUALENV="virtualenv --system-site-packages --distribute --prompt=($BASEPATH)"
PIP="pip --timeout 30 -q"
ENVDIR=env


echo "Checking PIP and virtualenv availability"
pip install 'pip>=1.1' 'virtualenv>=1.7.1.2'
if [ $? == 0 ]; then
    echo 'PIP and virtualenv installed allright'
else
    echo 'Error installing PIP and virtualenv, breaking off'
    echo 'Please execute the following command manually, and watch for errors:'
    echo "    pip install 'pip>=1.1' 'virtualenv>=1.7.1.2'"
    exit 1
fi


if [ ! -d $ENVDIR ]; then
    echo "Preparing virtualenv environment in $ENVDIR directory"    
    $VIRTUALENV $ENVDIR
fi
        
echo 'Installing required packages'
if $ENVDIR/bin/pip install -r requirements.txt; then
    echo 'That went allright, continue'
else
    echo 'Error installing dependencies, breaking off'
    exit 1
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
fi

if [ ! -f settings_secret.py ]; then
    echo
    echo 'Generating secret key in settings_secret.py.'
    SECRET_KEY=`$BASH runserver.sh generate_secret_key`
    
    echo "# Add passwords passwords and other secrets data in this file" >> settings_secret.py
    echo >> settings_secret.py
    echo "# Make this unique, and don't share it with anybody." >> settings_secret.py
    echo "SECRET_KEY = '$SECRET_KEY'" >> settings_secret.py
    echo >> settings_secret.py
fi

if [ ! -f database.sqlite ]; then
    echo 'No database found, running syncdb and migrate.'
    ./runserver.sh syncdb
    ./runserver.sh migrate
fi
