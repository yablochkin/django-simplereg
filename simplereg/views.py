# -*- coding: utf-8 -*-
from django.views.generic.simple import direct_to_template
from django.contrib.auth import authenticate, login, REDIRECT_FIELD_NAME
from django.http import HttpResponseRedirect
from simplereg.forms import RegForm


def registration(request, template_name='auth/registration.html',
            redirect_field_name=REDIRECT_FIELD_NAME,
            form_class=RegForm, extra_context=None,
            callback=None):

    redirect_to = request.REQUEST.get(redirect_field_name, '')

    form = form_class(request.POST or None)
    if form.is_valid():
        user = form.save(request)
        user = authenticate(username=request.POST['email'], password=request.POST['password'])
        login(request, user)

        if callback:
            callback(request, user)

        return HttpResponseRedirect(redirect_to)

    return direct_to_template(request, template_name, {
            'form': form
        })
