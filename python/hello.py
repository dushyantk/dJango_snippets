#!/usr/bin/env python

import sys
from django.conf import settings

# Settings' section contains everything from database and cache connections to
# static and uploaded resources. But here we have Debug mode ON and then
# urlpattern will do it's magic.
# We have here a nonrandom SECRET_KEY setting
# Which should not be used in a production environment
settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisthesecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


from django.conf.urls import url
from django.http import HttpResponse

#Typical content of views.py in a larger project
dief index(request):
    return HttpResponse('Hello dJango')

#Typical content of urls.py
urlpatterns = (
    url(r'^$', index),
)

#manage.py works somewhat like this
if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
