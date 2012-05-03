===================================
Django project-base
===================================
Base project for the Django project
-----------------------------------

Dependencies
------------
Dependencies will be automatically installed in a virtualenv environment in
the `env` directory upon running `prepare.sh`. As of now, the following
dependencies will be installed, from PyPI:

*   django-extensions (http://github.com/django-extensions/django-extensions/)
*   django-debug-toolbar (http://github.com/robhudson/django-debug-toolbar/)
*   raven (http://raven.readthedocs.org/en/latest/)

Usage
-----

Starting a project based on this project
========================================
	git init <my_project>
	
	cd <my_project>

	git pull git://github.com/dokterbob/django-project-base.git
	
	./prepare.sh
	
	./runserver.sh

Updating your project from the base
===================================
	git pull git://github.com/dokterbob/django-project-base.git
