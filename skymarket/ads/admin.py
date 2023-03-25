from django.contrib import admin

from skymarket.ads.models import Ad, Comment, Mymodel

admin.site.register(Ad, Comment, Mymodel)

