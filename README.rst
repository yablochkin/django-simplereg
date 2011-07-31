================
django-simplereg
================

Simple registration app with authentication by email.

How to use
==========

Step 1
******

::

    $ pip install django-imagekit

(or clone the source and put the imagekit module on your path)

Step 2
******

Add simplereg to INSTALLED_APPS in your settings.py

Step 3 
******

Set new authentication backend to allow login be email.

::

    AUTHENTICATION_BACKENDS = (
        'simplereg.backend.EmailAuthBackEnd',
        'django.contrib.auth.backends.ModelBackend',
    )

Step 4
******

Add views to urls.py

::

    from django.conf.urls.defaults import *
    from simplereg.forms import LoginForm
    
    urlpatterns = patterns('',
        url(r'^registration/$', 'simplereg.views.registration', name='registration'),
        url(r'^login/$', 'django.contrib.auth.views.login', {
                'authentication_form': LoginForm
            }, name='login'),
        
        ...
    
    )