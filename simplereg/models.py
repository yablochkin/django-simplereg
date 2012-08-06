# -*- coding: utf-8 -*-
from django.contrib.auth.models import User


User.__unicode__ = lambda x: x.email
