from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(HomePageModel)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Serial)
admin.site.register(Season)
admin.site.register(Episode)
admin.site.register(comments)
admin.site.register(comments_serial)