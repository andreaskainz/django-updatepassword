django-updatepassword
=====================

``django-updatepassword`` contains the ``updatepassword`` command extension
for the Django web framework. It allows setting the password of a user
non-interactively.


Installation
------------

Install the package with pip::

 $ pip install git+http://github.com/andreaskainz/django-updatepassword.git

and add ``'django_updatepassword'`` to ``INSTALLED_APPS`` in your Django
project settings file::

 INSTALLED_APPS = (
    ...
    'django_updatepassword',
 )

Invoke ``./manage.py help`` to verify that the command is available and
``./manage.py help commandname`` for more specific usage instructions.

