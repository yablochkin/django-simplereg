================
django-simplereg
================

Simple registration app with authentication by email.

How to use
==========

Step 1
******

::

    $ pip install -e git://github.com/Bers/django-simplereg.git#egg=simplereg

(or clone the source and put module on your path)

Step 2
******

Set new authentication backend to allow login be email.

::

    AUTHENTICATION_BACKENDS = (
        'simplereg.backend.EmailAuthBackEnd',
        'django.contrib.auth.backends.ModelBackend',
    )

Step 3
******

Add views to urls.py

::

    from django.conf.urls.defaults import *
    from simplereg.forms import LoginForm
    
    urlpatterns = patterns('',
        url(r'^registration/$', 'simplereg.views.registration', {
                'template_name': 'registration.html',
                'autologin': True,
                'callback': None
            }, name='registration'),
        url(r'^login/$', 'django.contrib.auth.views.login', {
                'authentication_form': LoginForm
            }, name='login'),
        
        ...
    
    )
